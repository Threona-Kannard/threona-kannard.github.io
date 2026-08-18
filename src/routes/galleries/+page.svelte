<script lang="ts">
    import { goto } from "$app/navigation";
    import { _, json } from "svelte-i18n";
    import Separator from "$lib/components/Separator.svelte";
    import Photography from "$lib/components/galleries/Photography.svelte";

    type GalleryItem = {
        title: string;
        date: string;
        images: string[];
        variant?: "default" | "featured" | "wide" | "tall";
    };

    const galleryItems = ($json("page.galleries.items") ?? []) as GalleryItem[];

    let showBackToTop = $state(false);

    const checkScrollBottom = () => {
        const grid = document.querySelector(".main-grid");
        if (!grid) return;

        const isNearBottom =
            grid.scrollTop + grid.clientHeight >= grid.scrollHeight - 24;
        showBackToTop = isNearBottom;
    };

    const scrollToTop = () => {
        const grid = document.querySelector(".main-grid");
        if (!grid) return;
        grid.scrollTo({ top: 0, behavior: "smooth" });
    };
</script>

<svelte:head>
    <title>{$_("page.galleries.title")}</title>
</svelte:head>

<div class="page-header">
    <button class="back-button" onclick={() => goto("/about?select=apps")}
        >← Back to inventory</button
    >
    <h1 class="title">{$_("page.galleries.title")}</h1>
</div>

<Separator />

<div class="main-grid scroll" onscroll={checkScrollBottom}>
    {#each galleryItems as item}
        <Photography
            title={item.title}
            date={item.date}
            images={item.images}
            variant={item.variant ?? "default"}
        />
    {/each}
</div>

{#if showBackToTop}
    <div class="floating-social-stack" aria-label="More photo links">
        <div class="social-nav">
            <div class="social-nav-title">
                <p>{$_("page.galleries.button.moreImages")}</p>
                <svg
                    class="social-nav-arrow"
                    fill="var(--color-fg)"
                    width="2rem"
                    height="2rem"
                    viewBox="0 0 12 20"
                    version="1.1"
                    xmlns="http://www.w3.org/2000/svg"
                    ><path
                        d="m 12.000001,8 v 4 H 8 v 4 H 4 v 4 H 0 V 0 h 4 v 4 h 4 v 4 z"
                    /></svg
                >
            </div>
            <div class="social-nav-link">
                <a
                    class="floating-social-button instagram"
                    href="https://www.instagram.com/threona.kannard/"
                    target="_blank"
                    rel="noreferrer"
                    aria-label="Open Instagram"
                    title="Instagram"
                >
                    <i class="fab fa-instagram"></i>
                </a>
                <a
                    class="floating-social-button tiktok"
                    href="https://www.tiktok.com/@threona.kannard"
                    target="_blank"
                    rel="noreferrer"
                    aria-label="Open TikTok"
                    title="TikTok"
                >
                    <i class="fab fa-tiktok"></i>
                </a>
            </div>
        </div>
        <button
            class="floating-back-top"
            type="button"
            onclick={scrollToTop}
            aria-label="Back to top"
        >
            <i class="fas fa-chevron-up"></i>
            <span>{$_("page.galleries.button.backtotop")}</span>
        </button>
    </div>
{/if}

<style>
    .social-nav {
        display: flex;
        justify-content: center;
        align-items: center;
        gap: 15px;
    }

    .social-nav-link {
        display: flex;
        flex-direction: column;
        gap: 15px;
    }

    .social-nav-title {
        display: flex;
    }

    .social-nav-arrow {
        height: 2rem;
        width: 2rem;
        top: 0;
        animation: projectArrow 2s ease infinite;
    }

    @keyframes projectArrow {
        0%,
        100% {
            transform: translateX(-5px);
        }
        50% {
            transform: translateX(5px);
        }
    }

    .floating-social-stack {
        position: fixed;
        right: 6rem;
        bottom: 5rem;
        z-index: 30;
        display: flex;
        flex-direction: column;
        align-items: stretch;
        gap: 0.6rem;
    }

    .floating-social-button,
    .floating-back-top {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        gap: 0.65rem;
        padding: 0.8rem 1rem;
        border: 1px solid var(--color-border);
        background: rgba(12, 12, 12, 0.82);
        color: var(--color-fg);
        backdrop-filter: blur(10px);
        -webkit-backdrop-filter: blur(10px);
        box-shadow: 0 10px 20px rgba(0, 0, 0, 0.2);
        cursor: pointer;
        transition:
            opacity 0.2s ease,
            transform 0.2s ease;
        text-decoration: none;
    }

    .floating-social-button {
        width: 2.9rem;
        height: 2.9rem;
        padding: 0;
        border-radius: 50%;
    }

    .floating-social-button:hover,
    .floating-back-top:hover {
        transform: translateY(-2px);
    }

    .floating-social-button i,
    .floating-back-top i {
        font-size: 1rem;
    }

    .floating-back-top span {
        font-size: 0.9rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
    }

    .floating-social-button.instagram {
        color: #f7f0ff;
    }

    .floating-social-button.tiktok {
        color: #f7f0ff;
    }

    .page-header {
        display: flex;
        flex-wrap: wrap;
        gap: var(--padding-s);
        align-items: center;
        justify-content: space-between;
    }

    .back-button {
        appearance: none;
        background: transparent;
        border: 1px solid var(--color-border);
        color: var(--color-fg);
        padding: 0.75rem 1rem;
        border-radius: var(--border-radius);
        cursor: pointer;
        transition:
            background-color 0.2s ease,
            color 0.2s ease;
    }

    .back-button:hover {
        background-color: var(--color-fg);
        color: var(--color-bg);
    }
    :root {
        scroll-behavior: smooth;
    }

    .main-grid {
        display: grid;
        grid-template-columns: repeat(1, minmax(0, 1fr));
        grid-auto-rows: minmax(250px, auto);
        grid-auto-flow: dense;
        gap: 0.5rem;
        max-height: 65vh;
    }

    @media (min-width: 768px) {
        .main-grid {
            grid-template-columns: repeat(2, minmax(0, 1fr));
        }
    }

    @media (min-width: 1024px) {
        .main-grid {
            grid-template-columns: repeat(4, minmax(0, 1fr));
        }
    }
</style>
