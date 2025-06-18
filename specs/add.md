# **Architectural Design Document (ADD)**

## **Markdown Text-to-Speech Reader**

Version: 1.0  
Date: June 18, 2025

## **1\. Introduction**

### **1.1. Purpose**

This document provides a comprehensive architectural design for the Markdown Text-to-Speech (TTS) Reader application. It translates the functional and non-functional requirements outlined in the Software Requirements Specification (SRS) into a detailed technical blueprint. This ADD is intended for the development team to guide the implementation process, ensuring the final product is robust, maintainable, and scalable within its defined scope.

### **1.2. Scope**

The scope of this design encompasses the frontend user interface, the backend service layer, and the integration with the local Piper TTS engine. It details the system's structure, component breakdown, data flow, API design, and key technical decisions.

## **2\. Architectural Goals and Constraints**

The architecture is designed to meet the following key goals and constraints derived from the SRS:

* **Responsiveness:** The system must provide a fluid user experience with minimal latency between user actions (like clicking "read from here") and system responses (audio playback and highlighting). This is a primary architectural driver.  
* **Privacy:** All text processing must occur locally. The architecture explicitly forbids sending user-provided content to any external, cloud-based services.  
* **Maintainability:** The codebase must be modular, well-documented, and easy to understand to facilitate future maintenance and enhancements.  
* **Usability:** The design must support an intuitive and straightforward user interface that provides clear, real-time feedback.  
* **Constraint: Local Single-User Focus:** The backend and TTS engine are designed for a single-user, local deployment. The architecture is not designed for a high-concurrency, multi-tenant environment.  
* **Constraint: Specified Technology Stack:** The architecture is built upon the prescribed stack: Vue.js 3 for the frontend, Python/Flask for the backend, and Piper for the TTS engine.

## **3\. System Architecture**

The application will be built on a classic **Client-Server Architecture**.

* **Client (Frontend):** A Single-Page Application (SPA) built with Vue.js 3\. It is responsible for all user interactions, rendering the UI, and managing the presentation layer.  
* **Server (Backend):** A lightweight web service built with Python and the Flask framework. Its sole responsibilities are to receive text from the client, interface with the local Piper TTS engine, and return the generated audio and timing data.

### **3.1. Architectural Diagram**

\+------------------------------------------------+      \+-------------------------------------------+  
|                  CLIENT                        |      |                 SERVER                    |  
|                (Vue.js 3\)                      |      |              (Python/Flask)               |  
\+------------------------------------------------+      \+-------------------------------------------+  
|                                                |      |                                           |  
|  \+------------------+     \+------------------+ |      |  \+------------------+                     |  
|  |  View Components |     |  State Manager   | |      |  |   API Controller |  \<-- (HTTP/REST)--\> |  
|  | (MarkdownInput,  |     | (Playback State, | |      |  |    (/api/tts)    |                     |  
|  |  ContentViewer)  |     |  Highlighting)   | |      |  \+--------+---------+                     |  
|  \+--------+---------+     \+--------+---------+ |      |           |                             |  
|           |                        |           |      |  \+--------v---------+                     |  
|  \+--------v------------------------v---------+ |      |  |   TTS Service    |                     |  
|  |           UI Event Bus / Service           | |      |  | (Business Logic) |                     |  
|  |  (Handles Clicks, Playback Commands)     | |      |  \+--------+---------+                     |  
|  \+--------------------------------------------+ |      |           | (subprocess call)           |  
|                                                |      |  \+--------v---------+                     |  
|  \+------------------+     \+------------------+ |      |  | Piper TTS Wrapper|                     |  
|  |  Markdown Parser |     | Audio Player &   | |      |  | (Manages Piper   |                     |  
|  |   (markdown-it)  |     |   Highlighter    | |      |  |  process I/O)    |                     |  
|  \+------------------+     \+------------------+ |      |  \+--------+---------+                     |  
|                                                |      |           |                             |  
\+------------------------------------------------+      |  \+--------v---------+                     |  
                                                        |  |  Local Piper TTS |                     |  
                                                        |  |     (Engine)     |                     |  
                                                        |  \+------------------+                     |  
                                                        \+-------------------------------------------+

### **3.2. Architectural Patterns**

* **Frontend (Client):** The Vue.js application will implicitly follow the **Model-View-ViewModel (MVVM)** pattern.  
  * **Model:** The application's reactive state (e.g., raw Markdown text, playback status, current word/line IDs).  
  * **View:** The HTML templates of the Vue components that bind to the ViewModel.  
  * **ViewModel:** The Vue component instances themselves, which contain the logic and expose the state to the View.  
* **Backend (Server):** The Flask application will use a simple **Layered Architecture**.  
  * **Presentation Layer:** The API Controller (routes.py) that handles incoming HTTP requests.  
  * **Service/Business Logic Layer:** The TTS Service (tts\_service.py) that contains the core logic for text processing and interaction with the Piper wrapper.  
  * **Integration Layer:** The Piper TTS Wrapper (piper\_wrapper.py) that abstracts the details of communicating with the Piper executable.

## **4\. Component Design**

### **4.1. Frontend Component Breakdown (Vue.js 3\)**

The frontend will be composed of several key components:

* **App.vue (Root Component):**  
  * **Responsibility:** Main application layout, orchestrates interactions between child components.  
  * **State:** Holds the primary application state, such as the raw Markdown input and the list of text blocks derived from the rendered content.  
* **MarkdownInput.vue:**  
  * **Responsibility:** Provides the \<textarea\> for user input and the "Render" button.  
  * **Events:** Emits a submit-markdown event with the raw text content.  
* **ContentViewer.vue:**  
  * **Responsibility:**  
    1. Receives rendered HTML as a prop.  
    2. Displays the formatted content to the user.  
    3. Listens for click events on words.  
    4. Dynamically applies/removes highlight-line and highlight-word CSS classes based on data from the state manager.  
  * **Events:** Emits a read-from-word event with the ID of the clicked word.  
* **PlaybackControls.vue:**  
  * **Responsibility:** Displays Play/Pause/Stop buttons.  
  * **State:** Binds to the global playback status (e.g., 'playing', 'paused', 'stopped').  
  * **Events:** Emits play, pause, and stop events.

### **4.2. Frontend State Management**

Given the application's scope, a full-fledged state management library like Vuex or Pinia is not immediately necessary. A simpler approach using Vue 3's **Composition API** will be employed.

* A usePlaybackStore.js composable will be created to manage the shared, reactive state.  
* **Reactive State Properties:**  
  * rawMarkdown: ref('')  
  * renderedContent: shallowRef(null) (A structured representation of the text)  
  * playbackStatus: ref('stopped') // 'stopped', 'playing', 'paused'  
  * currentLineId: ref(null)  
  * currentWordId: ref(null)  
  * audioQueue: ref(\[\])  
* This composable will expose methods like startPlayback(), pausePlayback(), stopPlayback(), requestNextAudioChunk(), etc.

### **4.3. Markdown Parsing Strategy**

To enable precise highlighting, the Markdown text must be rendered into HTML with identifiable elements. The markdown-it library will be used with custom rendering rules.

1. **Rule Overrides:** The default renderers for paragraphs and text will be overridden.  
2. **Structure:** Each line (approximated by block-level elements like \<p\>, \<li\>, \<h1\>, etc.) will be given a unique ID (e.g., data-line-id="line-N").  
3. **Word Wrapping:** Inside each line, every word will be wrapped in a \<span\> with a unique ID (e.g., data-word-id="word-M").

**Example Output HTML:**

\<p data-line-id="line-1"\>  
  \<span data-word-id="word-1"\>This\</span\>  
  \<span data-word-id="word-2"\>is\</span\>  
  \<span data-word-id="word-3"\>the\</span\>  
  \<span data-word-id="word-4"\>first\</span\>  
  \<span data-word-id="word-5"\>line.\</span\>  
\</p\>

### **4.4. Backend API Design (Python/Flask)**

The backend will expose a single, primary endpoint.

* **Endpoint:** POST /api/tts  
* **Purpose:** To convert a plain text string into audio data with word timings.  
* **Request Body (JSON):**  
  {  
    "text": "This is a sentence to be spoken.",  
    "voice": "en\_US-amy-medium" // Optional, for future enhancement  
  }

* **Success Response (200 OK) (JSON):**  
  {  
    "audioContent": "UklGRiS...// Base64 encoded WAV audio data",  
    "mimeType": "audio/wav",  
    "timings": \[  
      { "word": "This", "startTime": 0.0, "endTime": 0.21 },  
      { "word": "is", "startTime": 0.21, "endTime": 0.35 },  
      { "word": "a", "startTime": 0.35, "endTime": 0.40 },  
      { "word": "sentence", "startTime": 0.40, "endTime": 0.95 },  
      // ... and so on  
    \]  
  }

* **Error Response (e.g., 500 Internal Server Error):**  
  {  
    "error": "TTS engine failed to process the request."  
  }

### **4.5. Backend TTS Integration (Piper)**

A piper\_wrapper.py module will abstract the interaction.

* **Invocation:** It will use Python's subprocess.Popen to run the Piper executable as a persistent child process.  
* **Communication:**  
  * The wrapper will write the input text to the Piper process's stdin.  
  * Piper needs to be configured to output JSON containing the audio path and word timings. The wrapper will read this from Piper's stdout.  
  * The wrapper will then read the generated WAV file from the specified path, encode it in Base64, and package it with the timing data for the API response.  
* **Error Handling:** The wrapper will monitor stderr for errors from the Piper process and handle cases where the process crashes or fails to generate audio.

## **5\. Data Flow and Sequence Diagram**

**User Story: User Clicks a Word to Start Reading**

sequenceDiagram  
    participant User  
    participant CViewer as ContentViewer.vue  
    participant PStore as usePlaybackStore.js  
    participant API as Backend API (Flask)  
    participant Piper as Piper TTS Engine

    User-\>\>+CViewer: Clicks on a word (e.g., with data-word-id="word-15")  
    CViewer-\>\>+PStore: Calls startPlayback("word-15")  
    PStore-\>\>PStore: Sets playbackStatus to 'playing'  
    PStore-\>\>PStore: Gathers plain text from word-15 to end of paragraph  
    PStore-\>\>+API: POST /api/tts { text: "The text chunk..." }  
    API-\>\>+Piper: Invokes Piper with the text  
    Piper--\>\>-API: Generates audio.wav and timings.json  
    API-\>\>API: Reads files, encodes audio to Base64  
    API--\>\>-PStore: 200 OK { audioContent, timings }  
    PStore-\>\>PStore: Decodes Base64 audio into a Blob/AudioBuffer  
    PStore-\>\>PStore: Starts audio playback  
    PStore-\>\>PStore: Initiates highlighting loop based on timings  
    loop For each word in timings  
        PStore-\>\>PStore: setTimeout() to schedule next highlight  
        PStore-\>\>PStore: Updates currentWordId and currentLineId  
    end  
    Note right of PStore: ContentViewer reacts to\<br/\>ID changes and applies\<br/\>CSS classes for highlighting.

## **6\. Security Considerations**

* **Input Sanitization:** Although no HTML is being saved, user-provided Markdown will be rendered. To prevent potential Cross-Site Scripting (XSS) if the rendered HTML is mishandled, the markdown-it library will be configured to disable raw HTML rendering and sanitize any potentially dangerous attributes.  
  // Vue.js component  
  import MarkdownIt from 'markdown-it';  
  const md \= new MarkdownIt({  
    html: false, // Disable HTML tags in source  
    linkify: true,  
    typographer: true  
  });

* **Backend Validation:** The backend will validate that the text field in the request body is a simple string and does not contain unexpected objects or structures.

## **7\. Deployment and Environment**

* **Development:**  
  * The Vue.js frontend will be served by the Vite development server (npm run dev).  
  * The Flask backend will be run directly (flask run).  
  * A CORS policy will be configured on the Flask app to allow requests from the Vite dev server's origin (e.g., http://localhost:5173).  
  * The path to the Piper executable will be managed via an environment variable or a configuration file.  
* **Production (Conceptual):**  
  * The Vue.js application will be built into static assets (npm run build).  
  * A production-grade web server like Gunicorn or uWSGI will be used to run the Flask application.  
  * The static frontend assets can be served by the same backend process or by a reverse proxy like Nginx. Nginx would also handle proxying /api requests to the Flask application.

## **8\. Development Guidelines**

* **Version Control:** Git will be used. The **Gitflow** branching model (or a simplified version with main and feature branches) is recommended.  
* **Code Style:**  
  * **Python:** PEP 8 standards, enforced with linters like flake8 and formatters like black.  
  * **JavaScript/Vue:** Prettier and ESLint will be configured to maintain consistent code style.  
* **Testing:**  
  * **Unit Tests:** Vitest for Vue components (verifying event emissions, prop handling) and pytest for Python modules (testing the TTS service logic and Piper wrapper in isolation).  
  * **Integration Tests:** End-to-end tests using a framework like Cypress could be added to simulate user flows across the entire stack.
