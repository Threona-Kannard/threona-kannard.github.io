<script lang="ts">
    import { _ } from "svelte-i18n";
    import { goto } from "$app/navigation";
    import Separator from "$lib/components/Separator.svelte";
    import Game from "$lib/components/games/Game.svelte";
    // Images
    import NSImg from "$lib/assets/images/games/ninja_school.jpg?enhanced";
    import NSBgImg from "$lib/assets/images/games/ninja_school_bg.jpg?enhanced";
</script>

<svelte:head>
    <title>{$_("page.games.retro-games")}</title>
</svelte:head>

<div class="page-header">
    <div><button class="back-button" onclick={() => goto("/about?select=apps")}>← Back to inventory</button></div>
    <h1 class="title">{$_("page.games.retro-games")}</h1>
    <div class="page-actions">
        <button class="nav-button" onclick={() => goto("/games")}>Games →</button>
    </div>
</div>

<Separator />

<div class="game-list scroll">
    <Game name={"Ninja School 1-3"} img={NSImg} tier={"a"} background={NSBgImg} tag={["Action", "Adventure"]}/>
    
</div>

<style>
    .page-header {
        display: grid;
        grid-template-columns: 1fr auto 1fr;
        gap: var(--padding-s);
        align-items: center;
        width: 100%;
    }

    .page-header .title {
        justify-self: center;
        text-align: center;
    }

    .page-actions {
        display: flex;
        align-items: center;
        justify-self: end;
        gap: 0.75rem;
    }

    .nav-button,
    .back-button {
        appearance: none;
        background: transparent;
        border: 1px solid var(--color-border);
        color: var(--color-fg);
        padding: 0.75rem 1rem;
        border-radius: var(--border-radius);
        cursor: pointer;
        transition: background-color 0.2s ease, color 0.2s ease;
    }

    .nav-button:hover,
    .back-button:hover {
        background-color: var(--color-fg);
        color: var(--color-bg);
    }

    .game-list {
        display: flex;
        flex-direction: column;
        max-height:70vh;
        gap: var(--padding-s);
    }

    @media screen and (max-width: 720px) {
        .page-header {
            flex-direction: column;
            align-items: flex-start;
        }
    }
</style>
