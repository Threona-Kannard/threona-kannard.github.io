<script lang="ts">
    const {
        name,
        img,
        background,
        tier,
        tag,
        darkMode = false,
    }: {
        name: string;
        img: any;
        background: any;
        tier: "s" | "a" | "b";
        tag?: string | string[];
        darkMode?: boolean;
    } = $props();

    const tags = $derived(Array.isArray(tag) ? tag : tag ? [tag] : []);
</script>

<div class="game" style={`border-left: .5rem solid var(--tier-${tier});`}>
    <enhanced:img class="game-wallpaper" src={background} alt="" loading="lazy" />
    <div class="game-content">
        <div class="game-info">
            <enhanced:img
                class={darkMode ? "invert" : ""}
                src={img}
                alt=""
                loading="lazy"
            />
            <h2>{name}</h2>
        </div>

        <div class="game-tier">
            <h2 class="desktop-only">Tier</h2>
            <h2><span class="tier-letter">{tier}</span></h2>
        </div>
    </div>

    {#if tags.length}
        <div class="game-tags" aria-label={`${name} tags`}>
            {#each tags as item}
                <span class="game-tag">{item}</span>
            {/each}
        </div>
    {/if}
</div>

<style>
    :root {
        --tier-s: #dfcc6e;
        --tier-a: #8c8891;
        --tier-b: var(--color-fg);
        --tag-bg: #333333;
        --tag-border: #5c5c5c;
    }

    .game {
        position: relative;
        height: 5rem;
        display: flex;
        align-items: stretch;
        justify-content: space-between;
        padding: var(--padding-s);
        background-color: var(--color-dark);
        overflow: hidden;
        isolation: isolate;
        transition:
            height 0.45s cubic-bezier(0.22, 1, 0.36, 1),
            transform 0.25s ease,
            box-shadow 0.25s ease,
            background-color 0.25s ease;
    }

    .game:hover {
        height:28rem;
        transform: translateY(-2px);
        box-shadow: 0 8px 24px rgba(0, 0, 0, 0.22);
        background-color: rgba(25, 25, 25, 0.92);
    }

    .game-wallpaper {
        position: absolute;
        inset: 0;
        width: 100%;
        height: 100%;
        object-fit: fill;
        opacity: 0;
        transform: scale(1.12);
        transition: opacity 0.4s ease, transform 0.5s ease;
        filter: brightness(0.38) saturate(1.15);
        z-index: 0;
    }

    .game:hover .game-wallpaper {
        opacity: 1;
        transform: scale(1);
    }

    .game-content {
        position: relative;
        z-index: 1;
        width: 100%;
        display: flex;
        align-items: center;
        justify-content: space-between;
        gap: var(--padding-s);
        transition: align-items 0.3s ease;
    }

    .game:hover .game-content {
        align-items: flex-start;
    }

    .game-tags {
        position: absolute;
        left: var(--padding-m);
        right: var(--padding-m);
        bottom: var(--padding-m);
        z-index: 2;
        display: flex;
        flex-wrap: wrap;
        gap: 0.5rem;
        opacity: 0;
        transform: translateY(10px);
        transition: opacity 0.3s ease, transform 0.3s ease;
    }

    .game:hover .game-tags {
        opacity: 1;
        transform: translateY(0);
    }

    .game-tag {
        display: inline-flex;
        align-items: center;
        justify-content: center;
        padding: 0.35rem 0.8rem;
        border: 1px solid rgba(255, 255, 255, 0.28);
        background: rgba(0, 0, 0, 0.45);
        color: #f5f5f5;
        font-size: 0.68rem;
        letter-spacing: 0.12em;
        text-transform: uppercase;
    }

    .game-info,
    .game-tier {
        position: relative;
        z-index: 1;
    }

    .game-info {
        display: flex;
        align-items: center;
        gap: var(--padding-m);
        transition: transform 0.3s ease, opacity 0.3s ease;
        align-self: flex-start;
        margin-top: 0.15rem;
    }

    .game:hover .game-info {
        transform: translateY(-0.2rem);
    }

    .game-info enhanced\:img {
        height: 4rem;
        width: auto;
    }

    .game-tier {
        display: flex;
        align-items: center;
        gap: var(--padding-s);
        opacity: 0.9;
        transition: opacity 0.25s ease, transform 0.25s ease;
    }

    .game:hover .game-tier {
        opacity: 0;
        transform: translateY(-0.2rem);
    }

    /* TIERS */
    .tier-letter {
        text-transform: capitalize;
    }

    /* INVERT DARK IMAGES ON DARK MODE */
    @media (prefers-color-scheme: dark) {
        .invert {
            filter: invert();
        }
    }
</style>
