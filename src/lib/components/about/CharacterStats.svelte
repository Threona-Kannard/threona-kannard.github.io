<script>
    import { _ } from "svelte-i18n";
    import Separator from "../Separator.svelte";
    // Images
    import CharacterImg from "$lib/assets/images/lain_walk.webp";
</script>

<div class="about-character-view">
    <div class="about-character-img">
        <img
            src={CharacterImg}
            alt="Character walking"
        />
    </div>

    <Separator margin={false} />

    <div class="about-character-info">
        <span class="info-separator"
            ><b>{@html $_("page.about.stats.nick")}</b>
            <p>:</p>
            <p>Threona (テェリオナ)</p></span
        >
        <span class="info-separator"
            ><b>{@html $_("page.about.stats.class")}</b>
            <p>:</p>
            <p>Technical Artist</p></span
        >
        <span class="info-separator"
            ><b>{@html $_("page.about.stats.guild")}</b>
            <p>:</p>
            <p>Sparx* - A Virtuos Studio</p></span
        >
        <span class="info-separator"
            ><b>{@html $_("page.about.stats.realm")}</b>
            <p>:</p>
            <p>Viet Nam</p></span
        >
        <span class="info-separator"
            ><b>{@html $_("page.about.stats.level")}</b>
            <p>:</p>
            <p>Mid-level</p></span
        >
    </div>
    <Separator/>
    <span class="italic text-justify text-base font-bold">
        {@html $_("page.about.stats.creed")}
    </span>
</div>

<style>
    .about-character-view {
        height: 100%;
        width: 29rem;
        display: flex;
        flex-direction: column;
        gap: var(--padding-s);
        
        border-right: var(--border-width) solid var(--color-border);
        padding: var(--padding-m);
    }

    .info-separator {
        display: grid;
        grid-template-columns: 1fr min-content 3fr;
    }
    .info-separator p:last-child {
        text-align: right;
    }

    .about-character-img {
        height: 17.6rem;
        display: flex;
        justify-content: center;
    }
    .about-character-img img {
        height: 100%;
        width: auto;
    }
</style>
