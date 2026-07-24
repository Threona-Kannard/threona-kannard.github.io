<script lang="ts">
	import { _ } from "svelte-i18n";
    import Separator from "$lib/components/Separator.svelte";
	import Social from "$lib/components/contact/Social.svelte";
</script>

<svelte:head>z
    <title>{$_("page.contact.title")}</title>
</svelte:head>

<h1 class="title">{$_("page.contact.title")}</h1>

<Separator />

<div class="container">
	<Social socialApp={"Mail"} name={"Email"} linkText={"Threona Huynh"} link={"mailto:threonahuynh.contact@gmail.com"} />
	<Social socialApp={"LinkedIn"} name={"LinkedIn"} linkText={"Threona Huynh"} link={"https://www.linkedin.com/in/phat-tan-huynh/"} />
	<Social socialApp={"Bilibili"} name={"Bilibili"} linkText={"Threona Huynh"} link={"https://space.bilibili.com/123456789"} />
	<Social socialApp={"X"} name={"X"} linkText={"Threona Huynh 👾"} link={"https://twitter.com/notkimu"} />
	<Social socialApp={"Discord"} name={"Discord"} linkText={"Threona Huynh"} link={"https://discord.gg/"} />

</div>

<style>
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