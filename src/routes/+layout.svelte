<script lang="ts">
    import "$lib/i18n";
    import "../app.css";
    import { _, isLoading, locale } from "svelte-i18n";
    import Header from "$lib/components/Header.svelte";
    import Sidebar from "$lib/components/Sidebar.svelte";
    // Images
    import FrameImg from "$lib/assets/images/frame.webp";
    import GuraSpinImg from "$lib/assets/images/gawr-spin.gif";

    let { children } = $props();
    const loadingMessage = $derived($locale ? $_("page.background.loading") : "Waiting for the content to load...");
</script>

<div id="app">
    <img src={FrameImg} class="frame" alt="">
    <div class="polka"></div>
    <div class="crt"></div>

    {#if $isLoading || !$locale}
        <center class="loading-container">
            <img class="loading-img" src={GuraSpinImg} alt="" loading="lazy" />
            <h1>{loadingMessage}</h1>
        </center>
    {:else}
        <Header />
        <!-- <Sidebar /> -->
        <main>
            {@render children()}
        </main>
    {/if}
</div>

<style>
    .frame {
        position: fixed;
        top: 0;
        left: 0;
        height: 100dvh;
        width: 100dvw;

        pointer-events: none;
		transition: 0s;
        z-index: 999999999;
    }

    .polka {
        position: fixed;
        top: 0;
        left: 0;
        height: 100%;
        width: 100%;

        pointer-events: none;
        opacity: 0.3;
        background-image: url("/src/lib/assets/svg/polka-pattern.svg");
        mask-image: -moz-linear-gradient(
            180deg,
            transparent 60%,
            rgba(0, 0, 0, 1) 100%
        );
        mask-image: -webkit-linear-gradient(
            180deg,
            transparent 60%,
            rgba(0, 0, 0, 1) 100%
        );
        mask-image: linear-gradient(
            180deg,
            transparent 60%,
            rgba(0, 0, 0, 1) 100%
        );
        z-index: -1;
    }

      .crt {
            position: fixed;
            height: 100%;
            width: 100%;
            top:            0;
            left:           0;

            background:     repeating-linear-gradient(#0000001d, #0000001d 3px, #00000000 3px, #00000000 10px);
            pointer-events: none;

            animation:      scanlines-scroll 15s infinite linear;
            z-index:        1001;
        }

        @keyframes scanlines-scroll {
            0% {
            background-position: 0 0;
            }
            100% {
            background-position: 0 100px;
            }
        }

    main {
        display: flex;
        flex-direction: column;
        justify-content: center;
    }

    .loading-container {
        margin-top: 30vh;
    }

    .loading-img {
        width: clamp(7rem, 10vw, 15%);
    }
</style>
