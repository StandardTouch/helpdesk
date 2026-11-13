<template>
  <svg
    :class="customClass || 'h-8 w-8 shrink-0'"
    viewBox="0 0 40 40"
    fill="none"
    xmlns="http://www.w3.org/2000/svg"
  >
    <!-- Background rounded square with subtle border -->
    <rect width="40" height="40" rx="9" fill="#000000" />
    <!-- "S" in Brand Red #ED1D24 -->
    <text
      x="7"
      y="27"
      font-family="'Poppins', sans-serif"
      font-size="20"
      font-weight="900"
      fill="#ED1D24"
    >S</text>
    <!-- "T" in White -->
    <text
      x="19"
      y="27"
      font-family="'Poppins', sans-serif"
      font-size="20"
      font-weight="900"
      fill="#FFFFFF"
    >T</text>
    <!-- Mini emblem vortex dot -->
    <circle cx="31.5" cy="14" r="2.5" fill="#ED1D24" />
    <circle cx="31.5" cy="14" r="1.2" fill="#00C8FF" />
  </svg>
</template>

<script setup lang="ts">
defineProps<{
  customClass?: string;
}>();
</script>
