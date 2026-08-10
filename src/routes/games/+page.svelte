<script>
    import { _ } from "svelte-i18n";
    import Separator from "$lib/components/Separator.svelte";
</script>

<svelte:head>
    <title>{$_("page.games.title")}</title>
</svelte:head>

<h1 class="title">{$_("page.games.title")}</h1>

<Separator />

<div class="placeholder-grid">
    <section class="placeholder-section">
        <h2>{$_("page.games.retro-games")}</h2>
        <div class="placeholder-panel" aria-hidden="true"></div>
    </section>

    <section class="placeholder-section">
        <h2>{$_("page.games.games")}</h2>
        <div class="placeholder-panel" aria-hidden="true"></div>
    </section>
</div>

<style>
    .placeholder-grid {
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: var(--padding-x);
    }

    .placeholder-section {
        display: flex;
        flex-direction: column;
        gap: var(--padding-s);
    }

    h2 {
        color: var(--color-cream);
        font-family: "Chicago 12";
        font-size: clamp(1.25rem, 3vw, 2rem);
    }

    .placeholder-panel {
        min-height: 18rem;
        border: var(--border-width) dashed var(--color-border);
        background: var(--color-blue-retro);
    }

    @media screen and (max-width: 728px) {
        .placeholder-grid {
            grid-template-columns: 1fr;
        }
    }
</style>
