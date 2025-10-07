<script setup lang="ts">
  import { RouterLink, RouterView } from "vue-router";
  import clickSound from "@/assets/audio/click.mp3";
  import windowsErrorSound from "@/assets/audio/windowsErrorSound.mp3";

  let imageUrl = "/src/assets/img/sign-bg-white.png"
  let clickCounter = 0;
  function addClick() {
    clickCounter += 1;
    imageUrl = "/src/assets/img/sign-bg-white.png"
    if (clickCounter === 10) {
      const audio = new Audio(windowsErrorSound);
      audio.play();
      clickCounter = 0;
      imageUrl = "/src/assets/img/sign-bg.png"
    }
  }

  function playClickSound() {
    const audio = new Audio(clickSound);
    audio.play();
  }
</script>

<!-- Content -->
<template>
  <div class="global__container" @click="playClickSound()">
    <header>
      <RouterLink to="/">
        <button class="full-h flex a-center g-m" v-on:click="addClick()">
          <div class="full-h">
            <img :src="imageUrl" class="full-h" alt="Home icon" />
          </div>
          <h1>Threona Kannard</h1>
        </button>
      </RouterLink>
    </header>
    <div class="filler" />

    <RouterView />
  </div>

  <div class="retro-overlay screen-h screen-w" />
</template>

<!-- Styles -->
<style scoped>
  header {
    height:           3rem;
    width:            100dvw;
    position:         fixed;
    background-color: black;

    z-index: 999;
  }
  .filler {
    height: 3rem;
  }

  .retro-overlay {
    position:       fixed;
    top:            0;
    left:           0;

    background:     repeating-linear-gradient(#00000038, #00000038 2.3px, #00000000 2.3px, #00000000 10px);
    pointer-events: none;

    animation:      scanlines-scroll 15s infinite linear;
    z-index:        999999999;
  }

  @keyframes scanlines-scroll {
    0% {
      background-position: 0 0;
    }
    100% {
      background-position: 0 100px;
    }
  }
</style>