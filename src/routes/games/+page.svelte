<script>
    import { _ } from "svelte-i18n";
    import { goto } from "$app/navigation";
    import Separator from "$lib/components/Separator.svelte";
    import Game from "$lib/components/games/Game.svelte";
    // Images
    import Portal2Img from "$lib/assets/images/games/portal2.webp?enhanced";
    import PortalImg from "$lib/assets/images/games/portal_logo.webp?enhanced";
    import PortalBgImg from "$lib/assets/images/games/portal_background.jpg?enhanced";
    import Portal2BgImg from "$lib/assets/images/games/portal2_background.jpg?enhanced";
    import Ac1Img from "$lib/assets/images/games/ac1.png?enhanced";
    import Ac1BgImg from "$lib/assets/images/games/ac1_bg.jpg?enhanced";
    import TerraNilImg from "$lib/assets/images/games/terra_nil.png?enhanced";
    import TerraNilBgImg from "$lib/assets/images/games/terra_nil_bg.jpg?enhanced";
    import SFImg from "$lib/assets/images/games/Split_fiction.png?enhanced";
    import SFBgImg from "$lib/assets/images/games/Split_Fiction_bg.jpg?enhanced";
    import T8Img from "$lib/assets/images/games/Tekken8.webp?enhanced";
    import T8BgImg from "$lib/assets/images/games/tekken8_bg.jpg?enhanced";
</script>

<svelte:head>
    <title>{$_("page.games.title")}</title>
</svelte:head>

<div class="page-header">
    <div><button class="back-button" onclick={() => goto("/about?select=apps")}>← Back to inventory</button></div>
    <h1 class="title">{$_("page.games.games")}</h1>
    <div class="page-actions">
        <button class="nav-button" onclick={() => goto("/games/GameRetro")}>Retro Games →</button>
    </div>
</div>

<Separator />

<div class="game-list scroll">
    <Game name={"Portal"} img={PortalImg} tier={"s"} background={PortalBgImg} tag={["Puzzle", "FPS", "3D Platformer"]} />
    <Game name={"Portal 2"} img={Portal2Img} tier={"s"} background={Portal2BgImg} tag={["Puzzle", "FPS", "3D Platformer"]} />
    <Game name={"Assassin's Creed"} img={Ac1Img} tier={"s"} background={Ac1BgImg} tag={["Action", "Adventure", "Stealth", "Historical", "Parkour"]} />
    <Game name={"Terra Nil"} img={TerraNilImg} tier={"s"} background={TerraNilBgImg} tag={["Strategy", "Relaxing", "Puzzle", "City Builder", "Casual"]} />
    <Game name={"Split Fiction"} img={SFImg} tier={"s"} background={SFBgImg} tag={["Co-op", "Split Screen", "Puzzle", "Action"]} />
    <Game name={"Tekken 8"} img={T8Img} tier={"s"} background={T8BgImg} tag={["Fighting", "Action", "Multiplayer"]} />
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
