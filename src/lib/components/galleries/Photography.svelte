<script lang="ts">
    const {
        title,
        date,
        image,
        images = [],
        variant = "default",
    }: {
        title: string;
        date: string;
        image?: string;
        images?: string[];
        variant?: "default" | "featured" | "wide" | "tall";
    } = $props();

    const allImages = $derived(images.length ? images : image ? [image] : []);
    const isVideoSource = (source: string) =>
        /\.(mp4|webm|ogg|mov|avi)$/i.test(source);
    let currentIndex = $state(0);
    let modalIndex = $state(0);
    let modalOpen = $state(false);
    let modalAutoplay: number | undefined;
    let isHoveringModalStage = $state(false);
    let activeVideo: HTMLVideoElement | null = null;

    const pauseActiveVideo = () => {
        if (activeVideo) {
            activeVideo.pause();
            activeVideo.currentTime = 0;
            activeVideo = null;
        }
    };

    const playOnlyOneVideo = (video: HTMLVideoElement | null) => {
        if (!video) return;

        if (activeVideo && activeVideo !== video) {
            activeVideo.pause();
            activeVideo.currentTime = 0;
        }

        activeVideo = video;
        video.muted = true;
        video.playsInline = true;

        if (!modalOpen && video.dataset.preview === "preview") {
            return;
        }

        video.play().catch(() => {
            // browser autoplay policy may block; ignore silently
        });
    };

    const clearModalAutoplay = () => {
        if (modalAutoplay) {
            window.clearInterval(modalAutoplay);
            modalAutoplay = undefined;
        }
    };

    const startModalAutoplay = () => {
        clearModalAutoplay();

        if (!modalOpen || allImages.length <= 1 || isHoveringModalStage) return;

        const currentSource = allImages[modalIndex] ?? "";
        if (isVideoSource(currentSource)) return;

        modalAutoplay = window.setInterval(() => {
            if (!modalOpen || isHoveringModalStage) return;
            nextModalImage();
        }, 2000);
    };

    const nextPreviewImage = () => {
        if (allImages.length <= 1) return;
        currentIndex = (currentIndex + 1) % allImages.length;
    };

    const prevPreviewImage = () => {
        if (allImages.length <= 1) return;
        currentIndex = (currentIndex - 1 + allImages.length) % allImages.length;
    };

    const nextModalImage = () => {
        if (allImages.length <= 1) return;
        modalIndex = (modalIndex + 1) % allImages.length;
        startModalAutoplay();
    };

    const prevModalImage = () => {
        if (allImages.length <= 1) return;
        modalIndex = (modalIndex - 1 + allImages.length) % allImages.length;
        startModalAutoplay();
    };

    const openModal = () => {
        modalIndex = currentIndex;
        modalOpen = true;
        startModalAutoplay();
    };

    const closeModal = () => {
        modalOpen = false;
        clearModalAutoplay();
        pauseActiveVideo();
    };

    $effect(() => {
        if (allImages.length < 2 || modalOpen) return;

        const timer = window.setInterval(() => {
            const currentSource = allImages[currentIndex] ?? "";
            if (isVideoSource(currentSource)) return;
            nextPreviewImage();
        }, 3000);

        return () => window.clearInterval(timer);
    });

    $effect(() => {
        if (!modalOpen) return;

        const onKeyDown = (event: KeyboardEvent) => {
            if (event.key === "Escape") closeModal();
            if (event.key === "ArrowRight") {
                nextModalImage();
            }
            if (event.key === "ArrowLeft") {
                prevModalImage();
            }
        };

        window.addEventListener("keydown", onKeyDown);
        startModalAutoplay();

        return () => {
            window.removeEventListener("keydown", onKeyDown);
            clearModalAutoplay();
        };
    });
</script>

<section
    class={`photo-card photo-card--${variant}`}
    onclick={openModal}
    role="button"
    tabindex="0"
    onkeydown={(event) => {
        if (event.key === "Enter" || event.key === " ") {
            event.preventDefault();
            openModal();
        }
    }}
>
    {#key currentIndex}
        {#if isVideoSource(allImages[currentIndex] ?? image ?? "")}
            <video
                class="photo-media photo-media--video"
                src={allImages[currentIndex] ?? image ?? ""}
                muted
                playsinline
                preload="metadata"
                data-preview="preview"
                autoplay={false}
                onplay={(event) => playOnlyOneVideo(event.currentTarget)}
                onended={() => nextPreviewImage()}
            ></video>
        {:else}
            <div
                class="photo-media"
                style={`background-image: url(${allImages[currentIndex] ?? image ?? ""})`}
            ></div>
        {/if}
    {/key}
    <div class="content">
        <h1>{title}</h1>
        <h3>{date}</h3>
    </div>
    <div class="img-overlay">
        <div>
            <i class="fas fa-images"></i>
            <h2>View Project</h2>
        </div>
    </div>
</section>

{#if modalOpen && allImages.length}
    <div
        class="modal-backdrop"
        role="button"
        tabindex="0"
        onclick={closeModal}
        onkeydown={(event) => {
            if (event.key === "Enter" || event.key === " ") {
                event.preventDefault();
                closeModal();
            }
        }}
    >
        <div
            class="modal-window"
            role="dialog"
            aria-modal="true"
            aria-label={`${title} gallery`}
            onclick={(event) => event.stopPropagation()}
            onkeydown={(event) => {
                if (event.key === "Escape") closeModal();
            }}
            tabindex="0"
        >
            <div class="modal-header">
                <h2 class="modal-title">{title}</h2>
            </div>

            <div class="modal-body">
                <div
                    class="modal-stage"
                    role="presentation"
                    onmouseenter={() => {
                        isHoveringModalStage = true;
                        clearModalAutoplay();
                    }}
                    onmouseleave={() => {
                        isHoveringModalStage = false;
                        startModalAutoplay();
                    }}
                >
                    {#key modalIndex}
                        {#if isVideoSource(allImages[modalIndex])}
                            <video
                                class="modal-media modal-video"
                                src={allImages[modalIndex]}
                                muted
                                playsinline
                                preload="metadata"
                                autoplay={modalOpen}
                                onplay={(event) => playOnlyOneVideo(event.currentTarget)}
                                onended={() => nextModalImage()}
                            ></video>
                        {:else}
                            <img
                                class="modal-image"
                                src={allImages[modalIndex]}
                                alt={`${title} ${modalIndex + 1}`}
                            />
                        {/if}
                    {/key}
                </div>
            </div>

            <div class="modal-dots" aria-label="Image selector">
                {#each allImages as _, index}
                    <button
                        class:active={index === modalIndex}
                        type="button"
                        aria-label={`Show image ${index + 1}`}
                        onclick={() => (modalIndex = index)}
                    ></button>
                {/each}
            </div>

            <div class="modal-actions">
                <button
                    class="action-button nav-left"
                    type="button"
                    onclick={prevModalImage}
                    title="prev"
                >
                    <i class="fa-solid fa-angle-left"></i>
                </button>
                <button
                    class="action-button nav-right"
                    type="button"
                    onclick={nextModalImage}
                    title="next"
                >
                    <i class="fa-solid fa-angle-right"></i>
                </button>
            </div>
        </div>
    </div>
{/if}

<style>
    .photo-card {
        position: relative;
        display: flex;
        align-items: flex-end;
        min-height: 300px;
        overflow: hidden;
        border-radius: 2px;
        cursor: pointer;
        transition: transform 0.25s cubic-bezier(0.075, 0.82, 0.165, 1);
        outline: none;
    }

    .photo-media {
        position: absolute;
        inset: 0;
        background-size: cover;
        background-position: bottom;
        transform: translateX(40px);
        opacity: 0;
        animation: slideInFromRight 0.7s cubic-bezier(0.22, 1, 0.36, 1) forwards;
    }

    .photo-media--video,
    .modal-video {
        width: 100%;
        height: 100%;
        object-fit: cover;
        display: block;
    }

    .photo-card:focus-visible {
        box-shadow: 0 0 0 2px rgba(255, 255, 255, 0.8);
    }

    .photo-card:hover {
        transform: translateY(-2px);
    }

    .photo-card--wide {
        grid-column: span 1;
    }

    .photo-card--tall {
        grid-row: span 1;
    }

    .photo-card--featured {
        grid-column: span 1;
        grid-row: span 1;
    }

    @media (min-width: 768px) {
        .photo-card--wide {
            grid-column: span 2;
        }

        .photo-card--tall {
            grid-row: span 2;
        }

        .photo-card--featured {
            grid-column: span 2;
            grid-row: span 3;
        }
    }

    @media (min-width: 1024px) {
        .photo-card--featured {
            grid-column: span 2;
            grid-row: span 3;
        }
    }

    .content {
        position: absolute;
        left: 1rem;
        bottom: 1rem;
        z-index: 1;
        color: #f3f4f6;
        text-transform: uppercase;
    }

    .content h1,
    .content h3,
    .img-overlay h2 {
        margin: 0;
    }

    .content h1 {
        font-size: clamp(1.5rem, 2vw, 2.5rem);
        font-weight: 700;
        letter-spacing: 2px;
    }

    .content h3 {
        font-size: 1rem;
    }

    .img-overlay {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        background-color: rgba(0, 0, 0, 0.65);
        opacity: 0;
        transition: opacity 0.3s ease-in;
        display: flex;
        align-items: center;
        justify-content: center;
        text-align: center;
    }

    .img-overlay > div {
        color: #f3f4f6;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        gap: 0.5rem;
    }

    .img-overlay i {
        font-size: 3rem;
    }

    .img-overlay h2 {
        font-size: 1.5rem;
        letter-spacing: 2px;
    }

    .photo-card:hover .img-overlay,
    .photo-card:focus-visible + .modal-backdrop {
        opacity: 1;
    }

    .modal-backdrop {
        position: fixed;
        inset: 0;
        z-index: 50;
        display: flex;
        align-items: center;
        justify-content: center;
        padding: 1.5rem;
        background: rgba(10, 10, 10, 0.38);
        backdrop-filter: blur(10px) saturate(1.2);
        -webkit-backdrop-filter: blur(10px) saturate(1.2);
        background-size: 20px 20px;
        animation: fadeIn 0.3s forwards;
    }

    .modal-window {
        position: relative;
        width: min(92vw, 1280px);
        max-height: 90vh;
        background: rgba(51, 51, 51, 0.7);
        border: 8px solid rgba(255, 255, 255, 0.9);
        outline: 4px solid rgba(0, 0, 0, 0.9);
        box-shadow:
            0 0 0 4px rgba(0, 0, 0, 0.8),
            0 20px 50px rgba(0, 0, 0, 0.45);
        backdrop-filter: blur(12px) saturate(1.2);
        -webkit-backdrop-filter: blur(12px) saturate(1.2);
        padding: 1.25rem 1.25rem 1.3rem;
        display: grid;
        place-items: center;
        animation: slideDown 0.4s forwards;
        font-family: "VT323", "Courier New", monospace;
    }

    .modal-header {
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding-bottom: 0.6rem;
        margin-bottom: 0.85rem;
        border-bottom: 4px solid #fff;
    }

    .modal-title {
        margin: 0;
        color: var(--color-cream);
        font-size: clamp(2rem, 3.2vw, 3.2rem);
        letter-spacing: 2px;
        text-transform: uppercase;
        text-shadow: 4px 4px 0 #000;
    }

    .modal-icon {
        width: 2.5rem;
        height: 2.5rem;
        background-color: #ff5555;
        clip-path: polygon(50% 0%, 100% 50%, 50% 100%, 0% 50%);
        position: relative;
        box-shadow: 0 0 0 3px #000;
    }

    .modal-icon::after {
        content: "!";
        position: absolute;
        inset: 0;
        display: grid;
        place-items: center;
        color: #fff;
        font-size: 1.6rem;
        font-weight: 700;
    }

    .modal-body {
        width: 100%;
        background: rgba(17, 17, 17, 0.9);
        border: 4px solid #fff;
        padding: 0.8rem;
    }

    .modal-stage {
        position: relative;
        width: 100%;
        min-height: 260px;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(0, 0, 0, 0.3);
        overflow: hidden;
    }

    .modal-image,
    .modal-video {
        width: 100%;
        height: min(52vh, 600px);
        object-fit: scale-down;
        display: block;
        animation: slideInFromRight 0.7s cubic-bezier(0.22, 1, 0.36, 1) forwards;
    }

    .modal-nav {
        display: none;
    }

    .nav-button,
    .modal-close {
        border: 4px solid #000;
        color: #fff;
        cursor: pointer;
        background: rgba(255, 255, 255, 0.08);
    }

    .nav-button {
        position: static;
        width: 3rem;
        height: 3rem;
        font-size: 1.5rem;
        background: rgba(255, 255, 255, 0.14);
    }

    .modal-close {
        display: none;
    }

    .modal-dots {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.65rem;
        margin: 0.85rem 0 1rem;
        width: 100%;
    }

    .modal-dots button {
        width: 0.9rem;
        height: 0.9rem;
        border-radius: 0;
        border: 2px solid #fff;
        background: rgba(255, 255, 255, 0.35);
        cursor: pointer;
        transition: all 0.2s ease;
    }

    .modal-dots button.active {
        background: #fff;
        transform: scale(1.1);
    }

    .modal-actions {
        display: flex;
        justify-content: center;
        gap: 0.85rem;
        width: 100%;
    }

    .action-button {
        cursor: pointer;
        font-family: "VT323", "Courier New", monospace;
        font-size: 1.8rem;
        text-transform: uppercase;
        color: #000;
        min-width: 9.5rem;
        padding: 0.7rem 1.5rem;
        border: 4px solid #000;
        box-shadow: 0 5px 0 rgba(0, 0, 0, 0.8);
        transition:
            transform 0.1s ease,
            box-shadow 0.1s ease;
    }

    .action-button.nav-left {
        background: #5555ff;
        box-shadow: 0 5px 0 #3333aa;
    }

    .action-button.nav-right {
        background: #55ff55;
        box-shadow: 0 5px 0 #33aa33;
    }

    .action-button:hover {
        transform: translateY(2px);
    }

    .action-button:active {
        transform: translateY(5px);
        box-shadow: none;
    }

    @keyframes slideDown {
        0% {
            transform: translateY(-50px);
            opacity: 0;
        }
        100% {
            transform: translateY(0);
            opacity: 1;
        }
    }

    @keyframes fadeIn {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
    }

    @keyframes slideInFromRight {
        0% {
            opacity: 0;
            transform: translateX(40px);
            filter: blur(2px);
        }
        100% {
            opacity: 1;
            transform: translateX(0);
            filter: blur(0);
        }
    }
</style>
