<script lang="ts">
	// Images
	import LinkedInImg from "$lib/assets/images/contact/linkedin.png?enhanced";
	import WeChatImg from "$lib/assets/images/contact/wechat.png?enhanced";
	import XImg from "$lib/assets/images/contact/x_new.png?enhanced";
	import MailImg from "$lib/assets/images/contact/mail.png?enhanced";
	import ZaloImg from "$lib/assets/images/contact/zalo.png?enhanced";
	import StarImg from "$lib/assets/images/star.gif";

	type SocialApp = "WeChat" | "LinkedIn" | "X" | "Mail" | "Zalo";
	type Props = {
		socialApp: SocialApp;
		name: string;
		linkText: string;
		link: string;
	}

	const { socialApp, name, linkText, link }: Props = $props();
</script>

<a href={link} class="container" target="_blank">
	<div class="container__img">
		{#if socialApp === "WeChat"}
			<enhanced:img src={WeChatImg} alt="WeChat icon" />
		{:else if socialApp === "LinkedIn"}
			<enhanced:img src={LinkedInImg} alt="LinkedIn icon" />
		{:else if socialApp === "X"}
			<enhanced:img src={XImg} alt="X icon" />
		{:else if socialApp === "Mail"}
		<enhanced:img src={MailImg} alt="Email icon" />
		{:else if socialApp === "Zalo"}
			<enhanced:img src={ZaloImg} alt="Zalo icon" />
		{/if}
	</div>

	<div class="">
		<h2 class="text-3xl font-bold">{name}</h2>
		<h3 class="text-xl font-bold p-1">{linkText}</h3>
	</div>

	<img class="container__star" src={StarImg} alt="Mario Bros Star" />
</a>

<style>
	.container {
		position: relative;
		display: flex;
		flex-direction: row;
		flex-wrap: wrap;
		align-items: center;
		align-self: stretch;
		gap: var(--padding-);

		background: linear-gradient(var(--color-bg), var(--color-border)) center no-repeat;
		background-position: 0px 300px;
		border: var(--border-width) solid var(--color-fg);
		padding: var(--padding-m);
		text-decoration: none;
	}
	.container:hover {
		background-position: 0px 0px;
		box-shadow: 0 0 10px 1px var(--color-border);
		padding: var(--padding-m);
	}

	.container__img {
		width: 5rem;
	}
	.container__img img {
		height: auto;
		width: 100%;
	}

	/* .container:hover .container__text * {
		color: var(--color-bg);
	} */

	.container__star {
		height: 3.5rem;
		width: auto;
		position: absolute;
		right: -1.5rem;
		top: -1.5rem;

		display: none;
	}
	.container:hover .container__star {
		display: block;
	}

	/* RESPONSIVE */
	@media screen and (max-width: 728px) {
		.container {
			width: 100%;
		}
	}
</style>