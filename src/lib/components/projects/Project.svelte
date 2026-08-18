<script lang="ts">
    type ExternalProjectMeta = {
        title?: string;
        url?: string;
    };

    const {
        name,
        description,
        img,
        tags,
        images = [],
        imageTitles = {},
        externalUrl,
    }: {
        name: string;
        description: string;
        img: any;
        tags: string[];
        images?: string[];
        imageTitles?:
            | Record<number, { title?: string; link?: string; youtubeUrl?: string }>
            | Record<string, { title?: string; link?: string; youtubeUrl?: string }>
            | string[];
        externalUrl?: string | ExternalProjectMeta;
    } = $props();

    const normalizeExternalUrl = (
        value?: string | ExternalProjectMeta
    ): ExternalProjectMeta => {
        if (!value) return { title: "External project", url: "" };
        if (typeof value === "string") {
            return { title: "External project", url: value };
        }

        return {
            title: value.title ?? "External project",
            url: value.url ?? "",
        };
    };

    const externalProject = $derived(normalizeExternalUrl(externalUrl));
    const galleryImages = $derived(images.length ? images : img ? [img] : []);
    const modalGalleryImages = $derived(
        externalProject.url ? [...galleryImages, externalProject.url] : galleryImages
    );

    const getSlideMeta = (index: number) => {
        if (Array.isArray(imageTitles)) {
            return {
                title: imageTitles[index] ?? `${name} ${index + 1}`,
                link: "",
            };
        }

        const titleMap = imageTitles as Record<string, { title?: string; link?: string; youtubeUrl?: string }>;
        const slide = titleMap[String(index)] ?? {};

        return {
            title: slide.title ?? `${name} ${index + 1}`,
            link: slide.link ?? slide.youtubeUrl ?? "",
        };
    };
    let modalOpen = $state(false);
    let modalIndex = $state(0);
    let isZoomed = $state(false);
    let autoplayTimer: number | undefined;
    let isHoveringModalStage = $state(false);

    const clearAutoplay = () => {
        if (autoplayTimer) {
            window.clearInterval(autoplayTimer);
            autoplayTimer = undefined;
        }
    };

    const startAutoplay = () => {
        clearAutoplay();

        if (!modalOpen || modalGalleryImages.length <= 1 || isHoveringModalStage) return;

        autoplayTimer = window.setInterval(() => {
            if (!modalOpen || isHoveringModalStage) return;
            nextImage();
        }, 2000);
    };

    const openExternalProject = () => {
        if (!externalProject.url) return;
        window.open(externalProject.url, "_blank", "noopener,noreferrer");
        closeModal();
    };

    const openModal = () => {
        modalIndex = 0;
        isZoomed = false;
        modalOpen = true;
        startAutoplay();
    };

    const closeModal = () => {
        modalOpen = false;
        isZoomed = false;
        clearAutoplay();
    };

    const nextImage = () => {
        if (modalGalleryImages.length <= 1) return;
        modalIndex = (modalIndex + 1) % modalGalleryImages.length;
        isZoomed = false;
        startAutoplay();
    };

    const prevImage = () => {
        if (modalGalleryImages.length <= 1) return;
        modalIndex =
            (modalIndex - 1 + modalGalleryImages.length) %
            modalGalleryImages.length;
        isZoomed = false;
        startAutoplay();
    };

    const toggleZoom = (event: MouseEvent) => {
        event.preventDefault();
        event.stopPropagation();
        isZoomed = !isZoomed;
    };

    $effect(() => {
        if (!modalOpen) return;

        const onKeyDown = (event: KeyboardEvent) => {
            if (event.key === "Escape") closeModal();
            if (event.key === "ArrowRight") {
                nextImage();
                startAutoplay();
            }
            if (event.key === "ArrowLeft") {
                prevImage();
                startAutoplay();
            }
        };

        window.addEventListener("keydown", onKeyDown);
        startAutoplay();
        return () => {
            window.removeEventListener("keydown", onKeyDown);
            clearAutoplay();
        };
    });
</script>

<div
    class="accordion-section"
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
    <enhanced:img src={img} alt="" class="project-img" loading="lazy" />
    <p class="title-vertical">{name}</p>
    <div class="section-content">
        <h3 class="section-title">{name}</h3>
        <p class="section-description">
            {description}
        </p>
        <div class="project-tags">
            {#each tags as tag}
                <span>{tag}</span>
            {/each}
        </div>
        <button
            type="button"
            class="view-button"
            onclick={(event) => {
                event.stopPropagation();
                openModal();
            }}
        >
            View Project
        </button>
    </div>
</div>

{#if modalOpen}
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
            aria-label={`${name} details`}
            onclick={(event) => event.stopPropagation()}
            onkeydown={(event) => {
                if (event.key === "Escape") closeModal();
            }}
            tabindex="0"
        >
            <div class="modal-header">
                <div>
                    <p class="modal-kicker">Project</p>
                    <h2 class="modal-title">{name}</h2>
                </div>
                <button type="button" class="close-button" onclick={closeModal} title="closeBtn"
                    ><i class="fa-solid fa-xmark closeBtn-icon"></i></button
                >
            </div>

            {#if modalGalleryImages.length}
                <div class="modal-body" >
                    <div
                        class="modal-stage"
                        role="presentation"
                        onmouseenter={() => {
                            isHoveringModalStage = true;
                            clearAutoplay();
                        }}
                        onmouseleave={() => {
                            isHoveringModalStage = false;
                            startAutoplay();
                        }}
                    >
                        {#if modalIndex === modalGalleryImages.length - 1 && externalProject.url}
                            <div class="external-placeholder">
                                <p class="external-label">External Portfolio Link</p>
                                <h3>{externalProject.title}</h3>
                                <p>
                                    This project portfolio is hosted on another site and
                                    blocks inline embedding. Open it in a new
                                    tab to view the full content.
                                </p>
                                <button
                                    type="button"
                                    class="external-button"
                                    onclick={openExternalProject}
                                >
                                    Open in new tab
                                </button>
                            </div>
                        {:else}
                            <button
                                type="button"
                                class:zoomed={isZoomed}
                                class="modal-media-button"
                                aria-label={`View ${name} image ${modalIndex + 1}`}
                                aria-pressed={isZoomed}
                                onclick={toggleZoom}
                            >
                                <img
                                    class:zoomed={isZoomed}
                                    class="modal-image"
                                    src={modalGalleryImages[modalIndex]}
                                    alt={`${name} ${modalIndex + 1}`}
                                    draggable="false"
                                />
                            </button>
                        {/if}
                    </div>

                    <div class="modal-caption-row" role="article" onmouseenter={() => {
                            isHoveringModalStage = true;
                            clearAutoplay();
                        }}
                        onmouseleave={() => {
                            isHoveringModalStage = false;
                            startAutoplay();
                        }}>
                        <div class="modal-caption">
                            {#if modalIndex === modalGalleryImages.length - 1 && externalProject.url}
                                <!-- Keep empty for external project slide -->
                            {:else}
                                {@const currentSlide = getSlideMeta(modalIndex)}
                                <span>{currentSlide.title}</span>
                                {#if currentSlide.link}
                                    <a
                                        class="youtube-link"
                                        href={currentSlide.link}
                                        target="_blank"
                                        rel="noreferrer"
                                        onclick={(event) => event.stopPropagation()}
                                    >
                                        Watch on YouTube
                                    </a>
                                {/if}
                            {/if}
                        </div>
                        <div class="modal-dots" aria-label="Image selector">
                            {#each modalGalleryImages as _, index}
                                <button
                                    class:active={index === modalIndex}
                                    type="button"
                                    aria-label={index ===
                                        modalGalleryImages.length - 1 &&
                                    externalProject.url
                                        ? `Open external project`
                                        : `Show image ${index + 1}`}
                                    onclick={() => (modalIndex = index)}
                                ></button>
                            {/each}
                        </div>
                    </div>
                </div>

                <div class="modal-actions">
                    <button
                        class="action-button nav-left"
                        type="button"
                        onclick={prevImage}
                        aria-label="Previous image"
                    >
                        <i class="fa-solid fa-angle-left"></i>
                    </button>
                    <button
                        class="action-button nav-right"
                        type="button"
                        onclick={nextImage}
                        aria-label="Next image"
                    >
                        <i class="fa-solid fa-angle-right"></i>
                    </button>
                </div>
            {:else}
                <div class="modal-body plain-body">
                    <p>{description}</p>
                </div>
            {/if}
        </div>
    </div>
{/if}

<style>
    @media (max-width: 700px) {
        .accordion-section {
            height: 60px;
            margin: 4px 0;
            align-items: center;
            justify-content: center;
        }

        .accordion-section:hover {
            height: 240px;
        }

        .title-vertical {
            position: absolute;
            top: 50%;
            left: 50%;
            transform: translate(-50%, -50%) rotate(0deg);
            white-space: nowrap;
            font-size: 1.2rem;
            font-weight: 600;
            letter-spacing: 1px;
            opacity: 1;
            transition: opacity var(--transition-time) ease;
            text-transform: uppercase;
        }

        .section-content {
            padding: 1rem;
        }

        .section-title {
            font-size: 1.2rem;
        }

        .section-description {
            font-size: 0.8rem;
            max-height: 100px;
            overflow-y: auto;
        }
    }

    :root {
        --transition-time: 1s;
        --bg-color: #0f0f0f;
        --text-color: #e6e6e6;
        --accent-color: #2a2a2a;
        --hover-color: #363636;
        --highlight-color: #525252;
    }

    .accordion-section {
        position: relative;
        flex: 1;
        height: 90%;
        overflow: hidden;
        background-color: var(--accent-color);
        border-radius: 8px;
        margin: 0 4px;
        box-shadow: 0 4px 20px rgba(0, 0, 0, 0.15);
        display: flex;
        align-items: flex-end;
        cursor: default;
        transition: flex var(--transition-time) cubic-bezier(0.25, 1, 0.5, 1); /* Hidden delay reset immediately on open */

        &::before {
            content: "";
            position: absolute;
            top: -50%;
            left: -50%;
            width: 200%;
            height: 200%;
            background: linear-gradient(
                0deg,
                transparent,
                transparent 30%,
                color-mix(in srgb, var(--color-border) 35%, transparent)
            );
            transform: rotate(-45deg);
            transition: all 0.5s ease;
            opacity: 0;
        }

        &:hover::before {
            opacity: 1;
            transform: rotate(-45deg) translateY(150%);
        }
    }

    .accordion-section:first-child {
        margin-left: 1%;
    }

    .accordion-section:last-child {
        margin-right: 2%;
    }

    .accordion-section:hover {
        flex: 6;
        background-color: var(--hover-color);
        box-shadow: 0 0 20px var(--color-border);
    }

    .accordion-section:hover .section-content {
        opacity: 1;
        transform: translateY(0);
    }

    .accordion-section:hover .title-vertical {
        opacity: 0;
    }

    .accordion-section:hover .project-img {
        opacity: 0.2;
        transform: scale(1.05);
    }

    .accordion-section:hover .project-tags span {
        opacity: 1;
        transform: translateY(0);
    }

    .project-img {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        object-fit: fill;
        opacity: 0.1;
        transition: all var(--transition-time) ease;
        transform: scale(1.2);
    }

    .title-vertical {
        position: absolute;
        top: 90%;
        left: 10%;
        transform: rotate(-90deg);
        white-space: nowrap;
        font-size: 1.2rem;
        font-weight: 600;
        letter-spacing: 1px;
        opacity: 1;
        transition: opacity var(--transition-time) cubic-bezier(0.25, 1, 0.5, 1);
        text-transform: uppercase;
    }

    .section-content {
        padding: 1.5rem;
        width: 100%;
        z-index: 2;
        opacity: 0;
        transform: translateY(20px);
        transition: all var(--transition-time) ease;
        transition-delay: 0.1s;
        background: linear-gradient(to top, rgba(0, 0, 0, 0.8), transparent);
    }

    .section-title {
        font-size: 1.4rem;
        font-weight: 700;
        margin-bottom: 0.5rem;
        position: relative;
        display: inline-block;
    }

    .section-description {
        font-size: 0.85rem;
        line-height: 1.5;
        margin-bottom: 1rem;
        opacity: 0.9;
    }

    .project-tags {
        display: flex;
        flex-wrap: wrap;
        gap: 8px;
        margin-top: 1rem;
    }

    .project-tags span {
        font-size: 0.7rem;
        padding: 4px 10px;
        background-color: rgba(255, 255, 255, 0.1);
        border-radius: 20px;
        opacity: 0;
        transform: translateY(10px);
        transition: all 0.3s ease;
    }

    .project-tags span:nth-child(1) {
        transition-delay: 0.1s;
    }
    .project-tags span:nth-child(2) {
        transition-delay: 0.15s;
    }
    .project-tags span:nth-child(3) {
        transition-delay: 0.2s;
    }
    .project-tags span:nth-child(4) {
        transition-delay: 0.25s;
    }

    .view-button {
        display: inline-block;
        margin-top: 1.2rem;
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 1px;
        padding: 8px 16px;
        background-color: transparent;
        border: 1px solid var(--text-color);
        color: var(--text-color);
        cursor: pointer;
        transition: all 0.3s ease;
        text-decoration: none;
        position: relative;
        overflow: hidden;
    }

    .view-button::before {
        content: "";
        position: absolute;
        top: 0;
        left: -100%;
        width: 100%;
        height: 100%;
        background-color: var(--text-color);
        transition: all 0.3s ease;
        z-index: -1;
    }

    .view-button:hover {
        color: var(--bg-color);
    }

    .view-button:hover::before {
        left: 0;
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
        width: 50vw;
        max-height: 100vh;
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

    .modal-kicker {
        margin: 0;
        font-size: 0.72rem;
        letter-spacing: 0.12em;
        text-transform: uppercase;
        color: rgba(255, 255, 255, 0.75);
    }

    .modal-title {
        margin: 0.2rem 0 0;
        color: var(--color-cream);
        font-size: clamp(2rem, 3.2vw, 3.2rem);
        letter-spacing: 2px;
        text-transform: uppercase;
        text-shadow: 4px 4px 0 #000;
    }

    .close-button {
        cursor: pointer;
        background-color: var(--color-warning);
        height: 40px;
        width: 40px;
        border: 4px solid #000;
        box-shadow: 0 5px 0 rgba(0, 0, 0, 0.8);
        display: inline-flex;
        align-items: center;
        justify-content: center;
        transition:
            transform 0.1s ease,
            box-shadow 0.1s ease;

        &:hover {
            transform: translateY(2px);
        }

        &:active {
            transform: translateY(5px);
            box-shadow: none;
        }
    }

    .modal-body {
        width: 100%;
        background: rgba(17, 17, 17, 0.9);
        border: 4px solid #fff;
        padding: 0.8rem;
    }

    .external-placeholder {
        width: 100%;
        min-height: 600px;
        display: flex;
        flex-direction: column;
        align-items: center;
        justify-content: center;
        text-align: center;
        padding: 2rem 1.5rem;
        background: rgba(22, 22, 22, 0.8);
        font-size: 1rem;
        color: #f3f4f6;

        & h3 {
            font-size: 1.2rem;
            font-weight: bold;
            text-transform: uppercase;
        }
    }

    .external-label {
        margin: 0 0 0.75rem;
        font-size: 1.5rem;
        letter-spacing: 0.16em;
        text-transform: uppercase;
        color: rgba(255, 255, 255, 0.7);
    }

    .external-button {
        cursor: pointer;
        font-size: 1rem;
        text-transform: uppercase;
        margin-top: 10px;
        background-color: var(--color-cream);
        box-shadow: 0 5px 0 var(--color-cream);
        color: var(--color-bg);
        min-width: 9.5rem;
        padding: 0.7rem 1.5rem;
        border: 4px solid #000;
        transition:
            transform 0.1s ease,
            box-shadow 0.1s ease;

        &:hover {
            transform: translateY(2px);
        }

        &:active {
            transform: translateY(5px);
            box-shadow: none;
        }
    }

    .modal-stage {
        position: relative;
        width: 100%;
        min-height: 100%;
        display: flex;
        align-items: center;
        justify-content: center;
        background: rgba(0, 0, 0, 0.3);
        overflow: hidden;
    }

    .modal-media-button {
        width: 100%;
        border: 0;
        background: transparent;
        padding: 0;
        margin: 0;
        cursor: zoom-in;
        transition: transform 0.45s cubic-bezier(0.22, 1, 0.36, 1);
    }

    .modal-media-button.zoomed {
        cursor: zoom-out;
    }

    .modal-media-button:focus-visible {
        outline: 2px solid rgba(255, 255, 255, 0.8);
        outline-offset: 4px;
    }

    .modal-image {
        width: 100%;
        height: min(80vh, 600px);
        object-fit: cover;
        display: block;
        transform-origin: center center;
        transition:
            transform 0.7s cubic-bezier(0.22, 1, 0.36, 1),
            filter 0.4s ease;
        animation: slideInFromRight 0.7s cubic-bezier(0.22, 1, 0.36, 1) forwards;
    }

    .modal-image.zoomed {
        object-fit:scale-down;
        filter: saturate(1.08) contrast(1.03);
    }

    .modal-caption-row {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 1rem;
        flex-wrap: wrap;
        margin-top: 0.85rem;
        color: #f3f4f6;
    }

    .modal-caption {
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: 0.75rem;
        flex-wrap: wrap;
        color: rgba(255, 255, 255, 0.8);
    }

    .youtube-link {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 0.35rem 0.8rem;
        border: 2px solid #fff;
        background: rgba(255, 255, 255, 0.08);
        color: #fff;
        font-size: 0.7rem;
        letter-spacing: 0.08em;
        text-transform: uppercase;
        text-decoration: none;
        transition: background 0.2s ease;
    }

    .youtube-link:hover {
        background: rgba(255, 255, 255, 0.18);
    }

    .modal-dots {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 0.65rem;
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
        margin-top: 1rem;
    }

    .action-button {
        cursor: pointer;
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

    .plain-body {
        min-height: 220px;
        color: rgba(255, 255, 255, 0.8);
        display: grid;
        place-items: center;
        text-align: center;
    }

    @keyframes fadeIn {
        0% {
            opacity: 0;
        }
        100% {
            opacity: 1;
        }
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
