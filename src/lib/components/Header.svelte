<script lang="ts">
    import { get } from "svelte/store";
    import { locale } from "svelte-i18n";
    import { onMount } from "svelte";
    // Images
    import CoplandOsImg from "$lib/assets/images/copland.webp";
    import KimuFaceImg from "$lib/assets/images/kimucara.webp";

    let userLocale = $state(getLocale());

    onMount(() => {
        const savedLocale = localStorage.getItem("locale");
        if (savedLocale) {
            locale.set(savedLocale);
            userLocale = savedLocale;
        }
    });

    function getLocale(): string {
        const userLocale = get(locale)?.substring(0, 2);
        if (!(userLocale || userLocale === "en" || userLocale === "es")) {
            locale.set("en");
            return "en";
        }

        return userLocale;
    }

    function updateLocale() {
        const strippedLocale = userLocale.substring(0, 2);

        localStorage.setItem("locale", strippedLocale);
        locale.set(strippedLocale);
    }
</script>

<header>
    <a href="/" class="titlebar">
        <img class="titlebar-image" src={KimuFaceImg} alt="" />
        <h2 class="subtitle">Threona</h2>
    </a>

    <div class="social">
        <a aria-label="github" href="https://github.com/Threona-Kannard">
            <svg
                class="social-link"
                viewBox="0 0 20 20"
                version="1.1"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                ><g
                    stroke="none"
                    stroke-width="1"
                    fill="none"
                    fill-rule="evenodd"
                    ><g
                        class="social-link-color"
                        transform="translate(-140.000000, -7559.000000)"
                        ><g transform="translate(56.000000, 160.000000)"
                            ><path
                                d="M94,7399 C99.523,7399 104,7403.59 104,7409.253 C104,7413.782 101.138,7417.624 97.167,7418.981 C96.66,7419.082 96.48,7418.762 96.48,7418.489 C96.48,7418.151 96.492,7417.047 96.492,7415.675 C96.492,7414.719 96.172,7414.095 95.813,7413.777 C98.04,7413.523 100.38,7412.656 100.38,7408.718 C100.38,7407.598 99.992,7406.684 99.35,7405.966 C99.454,7405.707 99.797,7404.664 99.252,7403.252 C99.252,7403.252 98.414,7402.977 96.505,7404.303 C95.706,7404.076 94.85,7403.962 94,7403.958 C93.15,7403.962 92.295,7404.076 91.497,7404.303 C89.586,7402.977 88.746,7403.252 88.746,7403.252 C88.203,7404.664 88.546,7405.707 88.649,7405.966 C88.01,7406.684 87.619,7407.598 87.619,7408.718 C87.619,7412.646 89.954,7413.526 92.175,7413.785 C91.889,7414.041 91.63,7414.493 91.54,7415.156 C90.97,7415.418 89.522,7415.871 88.63,7414.304 C88.63,7414.304 88.101,7413.319 87.097,7413.247 C87.097,7413.247 86.122,7413.234 87.029,7413.87 C87.029,7413.87 87.684,7414.185 88.139,7415.37 C88.139,7415.37 88.726,7417.2 91.508,7416.58 C91.513,7417.437 91.522,7418.245 91.522,7418.489 C91.522,7418.76 91.338,7419.077 90.839,7418.982 C86.865,7417.627 84,7413.783 84,7409.253 C84,7403.59 88.478,7399 94,7399"
                            ></path></g
                        ></g
                    ></g
                ></svg
            >
        </a>

        <a aria-label="x com" href="https://x.com/ThreonaHuynh">
            <svg
                class="social-link"
                width="1200" height="1227"
                viewBox="0 0 1200 1227"
                fill="none"
                xmlns="http://www.w3.org/2000/svg"
                ><g
                    stroke="none"
                    stroke-width="1"
                    fill="none"
                    fill-rule="evenodd"
                    ><g
                        class="social-link-color"
                        transform="translate(-60.000000, -7521.000000)"
                        ><g transform="translate(56.000000, 160.000000)"
                            ><path
                                d="M714.163 519.284L1160.89 0H1055.03L667.137 450.887L357.328 0H0L468.492 681.821L0 1226.37H105.866L515.491 750.218L842.672 1226.37H1200L714.137 519.284H714.163ZM569.165 687.828L521.697 619.934L144.011 79.6944H306.615L611.412 515.685L658.88 583.579L1055.08 1150.3H892.476L569.165 687.854V687.828Z"
                                fill="social-link-color"
                            /></g
                        ></g
                    ></g
                ></svg
            >
        </a>

        <a
            aria-label="patreon server"
            href="https://www.patreon.com/cw/threona_techart"
        >
            <svg
                class="social-link social-link-color"
                version="1.1"
                id="Layer_1"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                x="0px"
                y="0px"
                viewBox="0 0 1080 1080"
                style="enable-background:new 0 0 1080 1080;"
                xml:space="preserve"
                ><path
                    d="M1033.05,324.45c-0.19-137.9-107.59-250.92-233.6-291.7c-156.48-50.64-362.86-43.3-512.28,27.2
	C106.07,145.41,49.18,332.61,47.06,519.31c-1.74,153.5,13.58,557.79,241.62,560.67c169.44,2.15,194.67-216.18,273.07-321.33
	c55.78-74.81,127.6-95.94,216.01-117.82C929.71,603.22,1033.27,483.3,1033.05,324.45z"
                /></svg
            >
        </a>

        <select
            name="lang"
            class="lang-selector"
            bind:value={userLocale}
            onchange={() => updateLocale()}
        >
            <option value="en">en</option>
            <option value="es">es</option>
        </select>
    </div>
</header>
<div class="spacer"></div>

<style>
    :root {
        --spacing: clamp(1.5rem, 2vw, 5rem);
    }

    header {
        position: fixed;
        top: 0;
        left: 0;
        height: calc(var(--header-height) + var(--spacing));
        width: 100%;

        display: flex;
        justify-content: space-between;
        align-items: center;

        background-color: var(--color-bg);
        border-bottom: var(--border-width) solid var(--color-border);
        padding: var(--padding-m) var(--padding-main-x);
        padding-top: calc(var(--spacing) + 1rem);

        z-index: 1000;
    }

    .titlebar {
        background: linear-gradient(transparent, var(--color-accent)) center
            no-repeat;
        background-position: 0px 100px;
        border-bottom: var(--border-width) solid transparent;
        border-top: var(--border-width) solid transparent;
        text-decoration: none;
        transition: 0.2s cubic-bezier(0, 1.8, 1, -1.51);
    }
    .titlebar:hover {
        background-position: 0px 7px;
        border-bottom: var(--border-width) solid var(--color-accent);
    }

    .titlebar,
    .social {
        display: flex;
        align-items: center;
        gap: var(--padding-m);
    }
    .titlebar,
    .titlebar-image {
        height: 100%;
    }

    .social-copland {
        height: 2rem;
    }

    .social-link {
        display: grid;
        place-content: center;
        height: 1.3em;
    }
    .social-link-color {
        fill: var(--color-border);
    }
    .social a:hover .social-link-color {
        fill: var(--color-accent);
    }

    .lang-selector {
        color: var(--color-border);
        font-weight: bold;
    }

    .spacer {
        height: calc(var(--header-height) + var(--spacing));
    }
</style>
