<script lang="ts">
    const {
        name,
        description,
        img,
        tags,
    }: { name: string; description: string; img: any; tags: string[] } =
        $props();
</script>

<div class="accordion-section">
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
        <a href="/" class="view-button">View Project</a>
    </div>
</div>

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
        transition:
            flex var(--transition-time) cubic-bezier(0.25, 1, 0.5, 1),
            visibility 0s linear 0s; /* Hidden delay reset immediately on open */

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

        &.hidden {
            flex: 0;
            visibility: hidden;

            transition:
                flex var(--transition-time) cubic-bezier(0.25, 1, 0.5, 1),
                visibility 0s linear var(--transition-time); /* Delays visibility:hidden until flex finishes */
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
        object-fit: cover;
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
</style>
