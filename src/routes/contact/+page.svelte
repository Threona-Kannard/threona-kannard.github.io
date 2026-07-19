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
	<Social socialApp={"WeChat"} name={"WeChat"} linkText={"Threona Huynh"} link={"https://weixin.qq.com/r/0vX8X8X8X8X8X8X8"} />
	<Social socialApp={"X"} name={"X"} linkText={"Threona Huynh 👾"} link={"https://twitter.com/notkimu"} />
	<Social socialApp={"Zalo"} name={"Zalo"} linkText={"Threona Huynh"} link={"https://zalo.me/0901234567"} />

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