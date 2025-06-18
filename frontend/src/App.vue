<script setup>
import MarkdownInput from './components/MarkdownInput.vue';
import ContentViewer from './components/ContentViewer.vue';
import PlaybackControls from './components/PlaybackControls.vue';
import { usePlaybackStore } from './composables/usePlaybackStore';

const store = usePlaybackStore();

async function handleRead(wordId) {
  const index = Number(wordId.split('-')[1]) - 1;
  const words = store.rawMarkdown.value.split(/\s+/).slice(index);
  await store.fetchAudioAndPlay(words.join(' '), index);
}
</script>

<template>
  <div id="app">
    <MarkdownInput />
    <ContentViewer @read-from-word="handleRead" />
    <PlaybackControls />
  </div>
</template>
