<script setup>
import { usePlaybackStore } from '../composables/usePlaybackStore';

const store = usePlaybackStore();
</script>

<template>
  <div class="playback-controls">
    <button
      @click="store.play"
      :disabled="store.isPlaying.value || !store.audio.value"
    >
      Play
    </button>
    <button @click="store.pause" :disabled="!store.isPlaying.value">
      Pause
    </button>
    <button @click="store.stop">Stop</button>
  </div>
</template>
