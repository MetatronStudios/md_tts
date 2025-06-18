<script setup>
import { ref } from 'vue';
import { createMarkdownParser } from '../utils/markdown';
import { usePlaybackStore } from '../composables/usePlaybackStore';

const store = usePlaybackStore();

const markdown = ref('');

// markdown-it instance with custom plugin to add line and word IDs
const md = createMarkdownParser();

function renderMarkdown() {
  store.rawMarkdown.value = markdown.value;
  store.renderedContent.value = md.render(markdown.value);
}
</script>

<template>
  <div class="markdown-input">
    <textarea v-model="markdown" rows="8" cols="40" />
    <button @click="renderMarkdown">Render</button>
  </div>
</template>
