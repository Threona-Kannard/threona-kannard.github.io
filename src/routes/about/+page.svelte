<script lang="ts">
    import { goto } from "$app/navigation";
    import { _ } from "svelte-i18n";
    import Separator from "$lib/components/Separator.svelte";
    import CharacterStats from "$lib/components/about/CharacterStats.svelte";
    import Tools from "$lib/components/about/Tools.svelte";
    import Apps from "$lib/components/about/Apps.svelte";
    import Inventory from "$lib/components/about/Inventory.svelte";
    import { onMount } from "svelte";

    let selectedProperty:
        "biography" | "skills and spells" | "forge tools" | "inventory" | "" =
        $state("biography");

    onMount(() => {
        if (window.innerWidth < 728) {
            selectedProperty = "";
        }

        const selectedPropName = new URLSearchParams(
            window.location.search
        ).get("select");

        switch (selectedPropName) {
            case "bio":
                selectedProperty = "biography";
                break;
            case "skills":
                selectedProperty = "skills and spells";
                break;
            case "tools":
                selectedProperty = "forge tools";
                break;
            case "apps":
                selectedProperty = "inventory";
                break;
            default:
                selectedProperty = "biography";
                break;
        }
    });
</script>

<svelte:head>
    <title>{$_("page.about.title")}</title>
</svelte:head>

<div class="page-header">
    <button class="back-button" onclick={() => goto("/")}>← Back to home</button>
    <h1 class="title">{$_("page.about.title")}</h1>
</div>

<Separator />

<div class="about">
    <div class="about-character">
        <!-- On mobile we hide the stats when other things are shown -->
        <div class={`${selectedProperty != "" ? "stats-responsive" : ""}`}>
            <CharacterStats />
        </div>

        <div class="about-character-selector">
            <button
                aria-label="character status"
                class={`${selectedProperty === "" ? "property-selector-active" : ""} about-character-property mobile-only`}
                onclick={() => (selectedProperty = "")}
            >
                <svg
                    class="property-selector"
                    viewBox="0 0 16 16"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <path
                        d="M9.00001 0H7.00001L5.51292 4.57681L0.700554 4.57682L0.0825195 6.47893L3.97581 9.30756L2.48873 13.8843L4.10677 15.0599L8.00002 12.2313L11.8933 15.0599L13.5113 13.8843L12.0242 9.30754L15.9175 6.47892L15.2994 4.57681L10.4871 4.57681L9.00001 0Z"
                    />
                </svg>
            </button>
            <button
                aria-label="biography"
                class={`${selectedProperty === "biography" ? "property-selector-active" : ""} about-character-property`}
                onclick={() => (selectedProperty = "biography")}
            >
                <svg
                    class="property-selector"
                    viewBox="0 0 16 16"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <path
                        d="M0 0h14v2h2v14H0V0zm2 2v12h12V4h-1.998V2H2zm2 6h8v2H4V8zm0-4h6v2H4V4z"
                        fill-rule="evenodd"
                    />
                </svg>
            </button>

            <button
                aria-label="skills and spells"
                class={`${selectedProperty === "skills and spells" ? "property-selector-active" : ""} about-character-property`}
                onclick={() => (selectedProperty = "skills and spells")}
            >
                <svg
                    class="property-selector"
                    viewBox="0 0 16 16"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <path
                        d="M0 0h16v16H0V0zm2 2v2h2V2H2zm4 0v2h8V2H6zM2 6v8h12V6H2z"
                        fill-rule="evenodd"
                    />
                </svg>
            </button>

            <button
                aria-label="applications"
                class={`${selectedProperty === "forge tools" ? "property-selector-active" : ""} about-character-property`}
                onclick={() => (selectedProperty = "forge tools")}
            >
                <svg
                    class="property-selector"
                    viewBox="0 0 16 16"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <path
                        d="M0 0h7v7H0V0zm2 2v3h3V2H2zM0 9h7v7H0V9zm9-9h7v7H9V0zm2 2v3h3V2h-3zM9 9h7v7H9V9zm2 2v3h3v-3h-3zm-9 0v3h3v-3H2z"
                        fill-rule="evenodd"
                    />
                </svg>
            </button>

            <button
                aria-label="inventory"
                class={`${selectedProperty === "inventory" ? "property-selector-active" : ""} about-character-property`}
                onclick={() => (selectedProperty = "inventory")}
            >
                <svg
                    class="property-selector"
                    viewBox="0 0 16 16"
                    xmlns="http://www.w3.org/2000/svg"
                >
                    <path
                        d="M8 8v5h4V8h-2V6H8v2zm-8 8h16V0H0v16zm2-2V2h12v12H2zM8 4h2V2H8v2zm2 2h2V4h-2v2zm-1 6v-2h2v2H9z"
                        fill-rule="evenodd"
                    />
                </svg>
            </button>
        </div>
    </div>

    <div class="about-showed-property">
        <h2>{selectedProperty}</h2>
        {#if selectedProperty === "biography"}
            <p>{@html $_("page.about.biography")}</p>
        {:else if selectedProperty === "skills and spells"}
            <Tools />
        {:else if selectedProperty === "forge tools"}
            <Apps />
        {:else if selectedProperty === "inventory"}
            <Inventory />
        {/if}
    </div>
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

    /* About info */
    .about {
        height: 40rem;
        display: flex;
        border: var(--border-width) solid var(--color-border);
        overflow: hidden;
    }

    .about-character {
        display: flex;
    }

    /* Buttons */
    .about-character-selector {
        width: 2rem;
    }

    .property-selector {
        width: 100%;
        fill: var(--color-fg);
    }
    .property-selector-active {
        background-color: var(--color-fg);
    }
    .property-selector-active svg {
        fill: var(--color-bg);
    }

    .about-character-property {
        display: grid;
        place-content: center;
        border: var(--border-width) solid var(--color-border);
        border-left: none;
        padding: var(--padding-s);
    }
    .about-character-property:nth-child(2) {
        border-top: none;
    }
    .about-character-property:not(:last-child) {
        border-bottom: none;
    }

    /* Showed Property */
    .about-showed-property {
        height: 100%;
        width: 100%;
        display: flex;
        flex-direction: column;
        gap: var(--padding-xl);
        padding: var(--padding-x);
        overflow-y: auto;
    }
    .about-showed-property h2 {
        text-transform: capitalize;
    }

    /* Responsiveness on the RPG stats */
    @media screen and (max-width: 728px) {
        .stats-responsive {
            width: 0;
            opacity: 0;
            pointer-events: none;
        }

        .about-character-property:nth-child(2) {
            border-top: var(--color-border) solid var(--border-width);
        }
        .about-character-property:nth-child(1) {
            border-top: none;
        }
    }
</style>
