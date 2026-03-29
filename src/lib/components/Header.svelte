<script lang="ts">
    import { get } from "svelte/store";
    import { locale } from "svelte-i18n";
    import { onMount } from "svelte";
    import jQuery from "jquery";
    // Images
    // TODO: Change the image to threona logo
    import KimuFaceImg from "$lib/assets/images/kimucara.webp";

    function setMenuAnimationState(isOpen: boolean) {
        const menuItems = jQuery(".list__ul").find("li");

        if (isOpen) {
            // Remove then re-add class to reliably restart keyframe animation.
            menuItems.removeClass("toggled");
            const firstItem = menuItems.get(0) as HTMLElement | undefined;
            if (firstItem) {
                void firstItem.offsetWidth;
            }
            menuItems.addClass("toggled");
            return;
        }

        menuItems.removeClass("toggled");
    }

    function OnTextClicked() {
        const menu = jQuery(".list__ul");
        const isOpening = !menu.is(":visible");

        jQuery(".placeholder").css("opacity", "0");
        menu.toggle(isOpening);
        setMenuAnimationState(isOpening);
    }

    function OnOptionItemClicked(selectedLocale: string) {
        userLocale = selectedLocale;
        updateLocale();

        jQuery(".placeholder").text(selectedLocale).css("opacity", "1");
        jQuery(`.list__ul button[data-locale='${selectedLocale}']`)
            .closest("li")
            .prependTo(".list__ul");
        jQuery(".list__ul").hide();
        setMenuAnimationState(false);
    }

    // jQuery("select").on("change", function (e) {
    //     // Set text on placeholder hidden element
    //     jQuery(".placeholder").text(jQuery(this).val() as string);

    //     // Animate select width as placeholder
    //     jQuery(this).animate({ width: jQuery(".placeholder").width() + "px" });
    // });

    let userLocale = $state(getLocale());

    onMount(() => {
        const savedLocale = localStorage.getItem("locale");
        if (
            savedLocale === "en" ||
            savedLocale === "vi" ||
            savedLocale === "jp"
        ) {
            locale.set(savedLocale);
            userLocale = savedLocale;
        }
    });

    function getLocale(): string {
        const currentLocale = get(locale)?.substring(0, 2);
        if (
            !(
                currentLocale === "en" ||
                currentLocale === "vi" ||
                currentLocale === "jp"
            )
        ) {
            locale.set("en");
            return "en";
        }

        return currentLocale;
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
        <a
            aria-label="Instagram"
            href="https://www.instagram.com/threona.huynh/"
        >
            <svg
                class="social-link"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 0 24 24"
                ><g class="social-link-color" fill="none" fill-rule="evenodd"
                    ><path
                        fill-rule="nonzero"
                        d="M12 2.163c3.204 0 3.584.012 4.85.07 1.366.062 2.633.334 3.608 1.308.975.975 1.246 2.242 1.308 3.608.058 1.266.07 1.646.07 4.851s-.012 3.585-.07 4.851c-.062 1.366-.334 2.633-1.308 3.608-.975.975-2.242 1.246-3.608 1.308-1.266.058-1.646.07-4.85.07s-3.585-.012-4.851-.07c-1.366-.062-2.633-.334-3.608-1.308-.975-.975-1.246-2.242-1.308-3.608C2.175 15.585 2.163 15.205 2.163 12s.012-3.584.07-4.85c.062-1.366.334-2.633 1.308-3.608.975-.975 2.242-1.246 3.608-1.308C8.415 2.175 8.795 2.163 12 2.163zm0-2.163C8.741 0 8.332.014 7.052.072 5.197.157 3.355.673 2.014 2.014.673 3.355.157 5.197.072 7.052.014 8.332 0 8.741 0 12c0 3.259.014 3.668.072 4.948.085 1.855.601 3.697 1.942 5.038 1.341 1.341 3.183 1.857 5.038 1.942C8.332 23.986 8.741 24 12 24s3.668-.014 4.948-.072c1.855-.085 3.697-.601 5.038-1.942 1.341-1.341 1.857-3.183 1.942-5.038.058-1.28.072-1.689.072-4.948s-.014-3.668-.072-4.948c-.085-1.855-.601-3.697-1.942-5.038C20.645.673 18.803.157 16.948.072 15.668.014 15.259 0 12 0zm0 5.838a6.162 6.162 0 1 0 0 12.324 6.162 6.162 0 0 0 0-12.324zm0 10.162a4 4 0 1 1 0-8 4 4 0 0 1 0 8zm6.406-11.845a1.44 1.44 0 1 0 0 2.881 1.44 1.44 0 0 0 0-2.881z"
                    /></g
                ></svg
            >
        </a>
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

        <div class="list">
            <button class="placeholder" onclick={OnTextClicked}
                >{userLocale}</button
            >
            <ul class="list__ul">
                <li>
                    <button
                        data-locale="en"
                        onclick={() => OnOptionItemClicked("en")}>en</button
                    >
                </li>
                <li>
                    <button
                        data-locale="vi"
                        onclick={() => OnOptionItemClicked("vi")}>vi</button
                    >
                </li>
                <li>
                    <button
                        data-locale="jp"
                        onclick={() => OnOptionItemClicked("jp")}>jp</button
                    >
                </li>
            </ul>
        </div>
    </div>
</header>
<div class="spacer"></div>

<style lang="scss">
    $dark: #555;
    $color--primary: hsla(269, 100%, 50%, 1);
    :root {
        --spacing: clamp(1.5rem, 2vw, 5rem);
    }

    .list {
        display: inline-block;
        position: relative;
        margin-top: 5px;
        ul {
            text-align: left;
            position: absolute;
            padding: 0;
            top: 0;
            left: 0;
            display: none;
        }
        li {
            display: block;
            position: relative;
            width: 30px;
            border-bottom: 4px solid;
            text-align: center;
            font-size: 1.2rem;
            background-color: #7e7d7d3b;
            border-radius: 15%;
            color: var(--color-border);
            cursor: pointer;

            &:global(.toggled) {
                @for $m from 1 through 3 {
                    &:nth-child(#{$m + 1}) {
                        animation: fadeInLeft 0s ease-out both;
                        transition-delay:
                            #{0.05 * $m}s,
                            0s;
                        border-left: 4px solid;
                        margin-left: #{1 * $m}rem;
                        margin-top: 0.2rem;
                    }
                }
            }

            &:hover {
                color: var(--color-accent);
                button {
                    color: var(--color-accent);
                }
            }
        }
    }

    @keyframes fadeInLeft {
        0% {
            opacity: 0;
            transform: translate3d(-100%, 0, 0);
        }
        100% {
            opacity: 1;
            transform: none;
        }
    }

    .placeholder {
        //visibility: hidden;
        //position: fixed;
        border-bottom: 4px solid;
        font-size: 1.2rem;
        color: var(--color-border);
        cursor: pointer;
        &:hover {
            color: var(--color-accent);
        }
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

    .spacer {
        height: calc(var(--header-height) + var(--spacing));
    }
</style>
