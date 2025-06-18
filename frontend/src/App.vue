<script setup>
import MarkdownInput from './components/MarkdownInput.vue';
import ContentViewer from './components/ContentViewer.vue';

function handleRead(wordId) {
  console.log('read from', wordId);
}
</script>

<template>
  <div id="app">
    <MarkdownInput />
    <ContentViewer @read-from-word="handleRead" />
  </div>
</template>
