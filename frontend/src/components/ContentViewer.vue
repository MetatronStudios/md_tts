<script setup>
import { computed, watch } from 'vue';
import { usePlaybackStore } from '../composables/usePlaybackStore';

const store = usePlaybackStore();
const emit = defineEmits(['read-from-word']);

const rendered = computed(() => store.renderedContent.value);

watch(
  () => store.currentLineId.value,
  (newId, oldId) => {
    if (oldId) {
      document
        .querySelector(`[data-line-id="${oldId}"]`)
        ?.classList.remove('highlight-line');
    }
    if (newId) {
      document
        .querySelector(`[data-line-id="${newId}"]`)
        ?.classList.add('highlight-line');
    }
  },
);

watch(
  () => store.currentWordId.value,
  (newId, oldId) => {
    if (oldId) {
      document
        .querySelector(`[data-word-id="${oldId}"]`)
        ?.classList.remove('highlight-word');
    }
    if (newId) {
      document
        .querySelector(`[data-word-id="${newId}"]`)
        ?.classList.add('highlight-word');
    }
  },
);

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
