# **Software Requirements Specification (SRS) \- Markdown Text-to-Speech Reader**

## **1\. Introduction**

This document outlines the software requirements for a Markdown Text-to-Speech (TTS) Reader application. The application aims to provide users with an accessible way to consume Markdown content by converting it into spoken audio, with visual cues to track reading progress. The primary focus is on enabling reading from user-provided Markdown text and utilizing a local TTS engine for processing.

## **2\. Purpose**

The purpose of this application is to enhance accessibility and user convenience by allowing users to listen to Markdown content. It aims to provide a seamless reading experience with visual feedback (highlighting) and the flexibility to start reading from any desired point within the rendered Markdown, leveraging a privacy-focused local TTS solution.

## **3\. Scope**

This document covers the functional and non-functional requirements for a web-based application that:

* Accepts Markdown text input from the user via a textarea.  
* Renders the input Markdown text into viewable HTML.  
* Allows users to initiate text-to-speech reading from a specific word/line within the rendered content.  
* Visually highlights the current line and current word being read.  
* Utilizes a local Text-to-Speech engine (e.g., Piper) via a backend service.  
* Provides basic audio playback controls.

This application **will not** fetch content from external URLs or function as a browser extension. All content will be provided directly by the user.

## **4\. Functional Requirements**

### **4.1 Markdown Input and Content Display**

* **FR-01: Markdown Input Area:** The application shall provide a textarea for the user to paste Markdown text.  
* **FR-02: Submit Markdown:** The application shall provide a button (e.g., "Render" or "Submit") to process the entered Markdown text.  
* **FR-03: Markdown Rendering:** Upon submission, the application shall render the Markdown text into HTML, displaying it in a readable format within its user interface. This rendered content should be structured to allow for line and word identification for highlighting.  
* **FR-04: Error Handling \- Empty Input:** The application shall display an informative message if the user attempts to submit an empty Markdown input.  
* **FR-05: Error Handling \- Rendering Issues:** The application shall gracefully handle and display messages for any errors encountered during Markdown parsing or rendering.

### **4.2 Reading Control**

* **FR-06: Read from Here:** The user shall be able to click on any word within the rendered Markdown content to initiate reading from that specific word.  
* **FR-07: Play/Pause/Stop Controls:** The application shall provide controls to play, pause, and stop the text-to-speech playback.  
* **FR-08: Progress Tracking:** The application shall visually indicate the current reading position.

### **4.3 Highlighting**

* **FR-09: Line Highlighting:** While text is being read, the application shall highlight the entire current line being read with a yellow background marker.  
* **FR-10: Word Highlighting:** While text is being read, the application shall highlight the current word being read within the current line with a green background marker.  
* **FR-11: Highlighting Reset:** All highlighting shall be removed when reading is stopped or a new reading session begins.

### **4.4 Local TTS Engine Integration**

* **FR-12: Backend TTS Interface:** The application shall utilize a backend service to interface with a local Text-to-Speech engine (e.g., Piper).  
* **FR-13: Text to Audio Conversion:** The backend service shall receive text segments from the frontend and convert them into audio (e.g., MP3, WAV) using the local TTS engine.  
* **FR-14: Audio Streaming/Transfer:** The backend service shall transfer the generated audio back to the frontend for playback. The chosen method (e.g., streaming, file transfer) should optimize for responsiveness.  
* **FR-15: Word Timings (if available):** The backend, if supported by the TTS engine (Piper), shall attempt to retrieve and send word timing information along with the audio to the frontend to facilitate accurate word highlighting synchronization.

### **4.5 Audio Playback**

* **FR-16: Audio Playback:** The frontend shall play the audio received from the backend.  
* **FR-17: Synchronization:** The word and line highlighting shall be synchronized as closely as possible with the audio playback.

## **5\. Non-Functional Requirements**

### **5.1 Performance**

* **NFR-01: Latency:** The latency between clicking "read from here" and the start of audio playback should be minimal, ideally less than 2 seconds, accounting for content parsing, Markdown rendering, and initial TTS processing.  
* **NFR-02: Highlighting Responsiveness:** Text highlighting should appear synchronously with the spoken words, with no noticeable lag.  
* **NFR-03: Resource Usage:** The application should optimize resource usage (CPU, memory) on both client and server sides, especially given the local TTS processing.

### **5.2 Usability**

* **NFR-04: Intuitive Interface:** The user interface shall be intuitive and easy to navigate for users of varying technical proficiency.  
* **NFR-05: Clear Feedback:** The application shall provide clear visual and auditory feedback for all user actions and system states (e.g., loading indicators, error messages, active highlighting).  
* **NFR-06: Accessibility:** The application should consider basic accessibility principles for web content.

### **5.3 Security**

* **NFR-07: Input Validation:** All user inputs shall be validated to prevent common web vulnerabilities (e.g., XSS, malicious Markdown).  
* **NFR-08: Data Privacy:** Since a local TTS engine is used, no text content should be sent to external cloud TTS services.

### **5.4 Maintainability**

* **NFR-09: Code Modularity:** The codebase shall be modular and well-structured to facilitate future enhancements and maintenance.  
* **NFR-10: Documentation:** Key components and APIs shall be well-documented.

### **5.5 Scalability (Local Context)**

* **NFR-11: Single-User Focus:** The backend TTS service is designed for a single-user local setup. While basic concurrent requests might be handled, it is not optimized for high-volume multi-user environments.

## **6\. Technical Stack**

Based on the requirements, especially the need for local TTS engine integration and the user's provided options, the following stack is chosen:

* **Frontend Framework:** Vue.js 3  
  * **Reasoning:** Offers a reactive, component-based architecture well-suited for dynamic UI updates like text highlighting and Markdown rendering. Its relatively low learning curve and strong community support make it a good choice for this interactive application.  
  * **Markdown Rendering:** A client-side Markdown parsing library (e.g., marked.js or markdown-it) will be used.  
* **Backend Framework:** Python (Flask)  
  * **Reasoning:** Python is excellent for scripting and integrating with local system processes. Flask is a lightweight web framework that is suitable for building simple APIs to communicate with the frontend and manage the Piper TTS engine.  
* **Text-to-Speech Engine:** Piper  
  * **Reasoning:** As requested by the user, Piper is a highly efficient, high-quality, and local TTS engine suitable for embedding within the backend service.

## **7\. High-Level Architecture**

The application will follow a client-server architecture:

\+-------------------+      HTTP/REST API      \+-----------------------+  
|                   | \<---------------------\> |                       |  
|     Frontend      |                         |        Backend        |  
|   (Vue.js 3\)      |                         |      (Python/Flask)   |  
|                   |                         |                       |  
| \- Markdown Input  |                         | \- TTS Orchestration   |  
| \- Markdown Render |                         | \- Audio Generation    |  
| \- Playback Ctrls  |                         | \- Word Timing Proc.   |  
| \- Highlighting    |                         \+-----------+-----------+  
\+-------------------+                                     |  
                                                          | Local Process/API  
                                                          v  
                                                  \+-----------------+  
                                                  |   Local TTS     |  
                                                  |   Engine (Piper)|  
                                                  \+-----------------+

### **Architecture Flow:**

1. **User Input:** The user pastes Markdown text into the textarea in the Vue.js frontend.  
2. **Markdown Submission:** The user clicks the "Submit" button.  
3. **Markdown Rendering:** The Vue.js frontend, using a Markdown rendering library, converts the Markdown text into HTML.  
4. **Content Display:** The Vue.js frontend displays the rendered HTML content. Each word/line will be wrapped in identifiable HTML elements to facilitate highlighting.  
5. **User Initiates Reading:** The user clicks on a word in the displayed rendered text. The frontend identifies the starting text segment (plain text derived from the rendered HTML).  
6. **TTS Request:** The frontend sends the plain text segment to the Python backend's TTS endpoint.  
7. **TTS Processing:** The Python backend invokes the local Piper TTS engine, passing the text. Piper generates audio and ideally provides word timing information.  
8. **Audio & Timings Transfer:** The backend sends the generated audio data (e.g., as a Base64 string or an audio stream) and word timings (if available) back to the frontend.  
9. **Audio Playback & Highlighting:** The frontend plays the audio. Using the word timings, it dynamically updates CSS classes on the corresponding words and lines in the *rendered HTML* to apply yellow and green highlighting in real-time.  
10. **Continuous Flow:** As one audio segment finishes, the frontend requests the next segment of text from the backend, continuing the process until reading is stopped or the end of the content is reached.

## **8\. User Interface (Conceptual)**

The UI will feature:

* A header area with the application title.  
* A large textarea for pasting Markdown content.  
* A "Render Markdown" or "Submit" button associated with the textarea.  
* A main display area where the Markdown content will be rendered as HTML, formatted for readability.  
* Basic playback controls (Play, Pause, Stop) positioned conveniently.  
* When reading, the rendered text area will dynamically update with yellow line highlighting and green word highlighting.  
* A small status message area for loading, errors, or current reading status.

## **9\. Data Model**

While a full database might not be strictly necessary for the core functionality, potential data models could include:

* **User Preferences (Local Storage):**  
  * voice\_selection: (String) e.g., 'en-US-Standard-C'  
  * reading\_speed: (Number) e.g., 1.0 (normal)  
  * highlight\_colors: (Object) e.g., { line: 'yellow', word: 'green' }  
  * last\_markdown\_input: (String) Stores the last Markdown text entered.

## **10\. Future Enhancements**

* **Voice Selection:** Allow users to select different voices provided by Piper (if multiple models are available and loaded).  
* **Reading Speed Control:** Implement controls for adjusting the reading speed.  
* **Volume Control:** Add a slider for audio volume adjustment.  
* **Dark Mode:** Provide a dark theme option for improved readability in low-light conditions.  
* **Persistence:** Save recently entered Markdown texts.  
* **Markdown Preview:** Offer a live preview of the Markdown as it's typed.  
* **Local TTS Engine Management:** Provide a basic UI to configure or manage the local Piper installation (e.g., path to executable, model selection).
