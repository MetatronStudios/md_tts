<script setup>
import { computed } from 'vue';
import { usePlaybackStore } from '../composables/usePlaybackStore';

const store = usePlaybackStore();
const emit = defineEmits(['read-from-word']);

const rendered = computed(() => store.renderedContent.value);

function handleClick(event) {
  const target = event.target.closest('[data-word-id]');
  if (target) {
    emit('read-from-word', target.getAttribute('data-word-id'));
  }
}
</script>

<template>
  <div class="content-viewer" v-html="rendered" @click="handleClick"></div>
</template>
