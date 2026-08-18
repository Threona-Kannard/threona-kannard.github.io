<script lang="ts">
    import { goto } from "$app/navigation";
    import { _ } from "svelte-i18n";
    import Separator from "$lib/components/Separator.svelte";
    import Social from "$lib/components/contact/Social.svelte";
</script>

<svelte:head
    >z
    <title>{$_("page.contact.title")}</title>
</svelte:head>

<div class="page-header">
    <button class="back-button" onclick={() => goto("/")}>← Back to home</button>
    <h1 class="title">{$_("page.contact.title")}</h1>
</div>

<Separator />

<div class="container">
    <Social
        socialApp={"Mail"}
        name={"Email"}
        linkText={"Threona Huynh"}
        link={"mailto:threonahuynh.contact@gmail.com"}
    />
    <Social
        socialApp={"LinkedIn"}
        name={"LinkedIn"}
        linkText={"Threona Huynh"}
        link={"https://www.linkedin.com/in/phat-tan-huynh/"}
    />
    <Social
        socialApp={"Bilibili"}
        name={"Bilibili"}
        linkText={"Threona Huynh"}
        link={"https://space.bilibili.com/3707039752653311"}
    />
    <Social
        socialApp={"X"}
        name={"X"}
        linkText={"Threona Huynh 👾"}
        link={"https://x.com/ThreonaHuynh"}
    />
    <Social
        socialApp={"Discord"}
        name={"Discord"}
        linkText={"Threona Huynh"}
        link={"https://discord.gg/bsPgpn9Mxvs"}
    />
</div>

<style>
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
        transition: background-color 0.2s ease, color 0.2s ease;
    }

    .back-button:hover {
        background-color: var(--color-fg);
        color: var(--color-bg);
    }

    .container {
        display: flex;
        align-items: center;
        justify-content: center;
        gap: var(--padding-x);
        max-width: 100%;
        margin-top: var(--padding-x);
    }

    @media screen and (max-width: 728px) {
        .container {
            flex-direction: column;
        }
    }
</style>
