<template>
  <div class="inline-flex items-center gap-2 select-none">
    <!-- Stylized StandardTouch Logo SVG -->
    <svg
      :class="customClass || 'h-8 w-auto'"
      viewBox="0 0 240 52"
      fill="none"
      xmlns="http://www.w3.org/2000/svg"
    >
      <!-- "Standard" text in Brand Red #ED1D24 -->
      <text
        x="0"
        y="30"
        font-family="'Poppins', sans-serif"
        font-size="28"
        font-weight="800"
        letter-spacing="-0.5px"
        fill="#ED1D24"
      >Standard</text>

      <!-- "T" in Brand Black #000000 -->
      <text
        x="132"
        y="30"
        font-family="'Poppins', sans-serif"
        font-size="28"
        font-weight="800"
        letter-spacing="-0.5px"
        :fill="dark ? '#FFFFFF' : '#000000'"
      >T</text>

      <!-- Swirl / Vortex "o" -->
      <g transform="translate(150.5, 12)">
        <!-- Outer colored gradient swirl ring -->
        <circle cx="9" cy="9" r="8.5" stroke="#ED1D24" stroke-width="2.5" fill="none" />
        <path
          d="M9 1.5 A7.5 7.5 0 0 1 16.5 9"
          stroke="#0066FF"
          stroke-width="2.5"
          stroke-linecap="round"
          fill="none"
        />
        <path
          d="M16.5 9 A7.5 7.5 0 0 1 9 16.5"
          stroke="#00C8FF"
          stroke-width="2.5"
          stroke-linecap="round"
          fill="none"
        />
        <circle cx="9" cy="9" r="3.2" fill="#ED1D24" />
      </g>

      <!-- "uch" in Brand Black #000000 -->
      <text
        x="171"
        y="30"
        font-family="'Poppins', sans-serif"
        font-size="28"
        font-weight="800"
        letter-spacing="-0.5px"
        :fill="dark ? '#FFFFFF' : '#000000'"
      >uch</text>

      <!-- "e-Solutions" text -->
      <text
        x="133"
        y="45"
        font-family="'Montserrat', sans-serif"
        font-size="12.5"
        font-weight="700"
        font-style="italic"
        letter-spacing="0.2px"
        :fill="dark ? '#E2E8F0' : '#818285'"
      >e-Solutions</text>
    </svg>
  </div>
</template>

<script setup lang="ts">
defineProps<{
  dark?: boolean;
  customClass?: string;
}>();
</script>
