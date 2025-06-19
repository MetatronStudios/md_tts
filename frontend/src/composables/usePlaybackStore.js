import { ref, shallowRef } from 'vue';

const API_BASE = import.meta.env.VITE_API_URL || '';

const rawMarkdown = ref('');
const renderedContent = shallowRef('');
const currentLineId = ref(null);
const currentWordId = ref(null);
const audio = shallowRef(null);
const timings = shallowRef([]);
const isPlaying = ref(false);
const wordOffset = ref(0);
let highlightTimeouts = [];

function clearHighlight() {
  currentLineId.value = null;
  currentWordId.value = null;
}

function stop() {
  if (audio.value) {
    audio.value.pause();
    audio.value.currentTime = 0;
  }
  isPlaying.value = false;
  highlightTimeouts.forEach((id) => clearTimeout(id));
  highlightTimeouts = [];
  clearHighlight();
}

function play() {
  if (!audio.value) return;
  isPlaying.value = true;
  const startHighlights = () => {
    highlightTimeouts = timings.value.map((t, idx) =>
      setTimeout(() => {
        const wordId = `word-${wordOffset.value + idx + 1}`;
        currentWordId.value = wordId;
        const el = document.querySelector(`[data-word-id="${wordId}"]`);
        currentLineId.value =
          el?.closest('[data-line-id]')?.getAttribute('data-line-id') || null;
      }, t.startTime * 1000),
    );
  };

  if (audio.value.readyState >= HTMLMediaElement.HAVE_ENOUGH_DATA) {
    startHighlights();
  } else {
    audio.value.addEventListener('playing', startHighlights, { once: true });
  }

  audio.value.play();
  audio.value.onended = stop;
}

async function fetchAudioAndPlay(text, offset = 0) {
  const resp = await fetch(`${API_BASE}/tts`, {
    method: 'POST',
    headers: { 'Content-Type': 'application/json' },
    body: JSON.stringify({ text }),
  });
  const data = await resp.json();
  const url = `data:${data.mimeType};base64,${data.audioContent}`;
  audio.value = new Audio(url);
  timings.value = data.timings;
  wordOffset.value = offset;
  play();
}

export function usePlaybackStore() {
  return {
    rawMarkdown,
    renderedContent,
    currentLineId,
    currentWordId,
    audio,
    timings,
    isPlaying,
    fetchAudioAndPlay,
    play,
    pause: () => audio.value?.pause(),
    stop,
  };
}
