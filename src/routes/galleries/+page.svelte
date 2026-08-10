<script>
    import { _ } from "svelte-i18n";
    import Separator from "$lib/components/Separator.svelte";
</script>

<svelte:head>
    <title>{$_("page.galleries.title")}</title>
</svelte:head>

<h1 class="title">{$_("page.galleries.title")}</h1>

<Separator />

<div class="gallery-placeholder" aria-hidden="true"></div>

<style>
    .gallery-placeholder {
        min-height: 24rem;
        border: var(--border-width) dashed var(--color-border);
        background: var(--color-blue-retro);
    }
</style>
