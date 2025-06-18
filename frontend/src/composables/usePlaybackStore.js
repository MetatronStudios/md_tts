import { ref, shallowRef } from 'vue';

const rawMarkdown = ref('');
const renderedContent = shallowRef('');
const currentLineId = ref(null);
const currentWordId = ref(null);

export function usePlaybackStore() {
  return {
    rawMarkdown,
    renderedContent,
    currentLineId,
    currentWordId,
  };
}
