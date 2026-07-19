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
        if (!(
            currentLocale === "en" ||
            currentLocale === "vi" ||
            currentLocale === "jp"
        )) {
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
            aria-label="Linkedin"
            href="https://www.linkedin.com/in/phat-tan-huynh/"
            target="_blank"
        >
            <svg
                class="social-link"
                xmlns="http://www.w3.org/2000/svg"
                viewBox="0 4 15 15"
                width="35px"
                height="45px"
                ><g class="social-link-color" fill="none" fill-rule="evenodd"
                    ><path
                        d="M18.72 3.99997H5.37C5.19793 3.99191 5.02595 4.01786 4.86392 4.07635C4.70189 4.13484 4.55299 4.22471 4.42573 4.34081C4.29848 4.45692 4.19537 4.59699 4.12232 4.75299C4.04927 4.909 4.0077 5.07788 4 5.24997V18.63C4.01008 18.9901 4.15766 19.3328 4.41243 19.5875C4.6672 19.8423 5.00984 19.9899 5.37 20H18.72C19.0701 19.9844 19.4002 19.8322 19.6395 19.5761C19.8788 19.32 20.0082 18.9804 20 18.63V5.24997C20.0029 5.08247 19.9715 4.91616 19.9078 4.76122C19.8441 4.60629 19.7494 4.466 19.6295 4.34895C19.5097 4.23191 19.3672 4.14059 19.2108 4.08058C19.0544 4.02057 18.8874 3.99314 18.72 3.99997ZM9 17.34H6.67V10.21H9V17.34ZM7.89 9.12997C7.72741 9.13564 7.5654 9.10762 7.41416 9.04768C7.26291 8.98774 7.12569 8.89717 7.01113 8.78166C6.89656 8.66615 6.80711 8.5282 6.74841 8.37647C6.6897 8.22474 6.66301 8.06251 6.67 7.89997C6.66281 7.73567 6.69004 7.57169 6.74995 7.41854C6.80986 7.26538 6.90112 7.12644 7.01787 7.01063C7.13463 6.89481 7.2743 6.80468 7.42793 6.74602C7.58157 6.68735 7.74577 6.66145 7.91 6.66997C8.07259 6.66431 8.2346 6.69232 8.38584 6.75226C8.53709 6.8122 8.67431 6.90277 8.78887 7.01828C8.90344 7.13379 8.99289 7.27174 9.05159 7.42347C9.1103 7.5752 9.13699 7.73743 9.13 7.89997C9.13719 8.06427 9.10996 8.22825 9.05005 8.3814C8.99014 8.53456 8.89888 8.6735 8.78213 8.78931C8.66537 8.90513 8.5257 8.99526 8.37207 9.05392C8.21843 9.11259 8.05423 9.13849 7.89 9.12997ZM17.34 17.34H15V13.44C15 12.51 14.67 11.87 13.84 11.87C13.5822 11.8722 13.3313 11.9541 13.1219 12.1045C12.9124 12.2549 12.7546 12.4664 12.67 12.71C12.605 12.8926 12.5778 13.0865 12.59 13.28V17.34H10.29V10.21H12.59V11.21C12.7945 10.8343 13.0988 10.5225 13.4694 10.3089C13.84 10.0954 14.2624 9.98848 14.69 9.99997C16.2 9.99997 17.34 11 17.34 13.13V17.34Z"
                    /></g
                ></svg
            >
        </a>
        <a
            aria-label="github"
            href="https://github.com/Threona-Kannard"
            target="_blank"
        >
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
            aria-label="X"
            href="https://x.com/ThreonaHuynh"
            target="_blank"
        >
            <svg
                class="social-link social-link-color"
                version="1.1"
                id="Layer_1"
                xmlns="http://www.w3.org/2000/svg"
                xmlns:xlink="http://www.w3.org/1999/xlink"
                x="0px"
                y="0px"
                viewBox="0 0 30 25"
                style="enable-background:new 0 0 30 25;"
                xml:space="preserve"
                width="25px"
                height="45px"
            >
                <path d="M26.37,26l-8.795-12.822l0.015,0.012L25.52,4h-2.65l-6.46,7.48L11.28,4H4.33l8.211,11.971L12.54,15.97L3.88,26h2.65 l7.182-8.322L19.42,26H26.37z M10.23,6l12.34,18h-2.1L8.12,6H10.23z"/>
            </svg>
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
        border-bottom: 2px solid;
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

    .subtitle {
        color: var(--color-border);
    }
    .social a:hover .social-link-color {
        fill: var(--color-accent);
    }

    .spacer {
        height: calc(var(--header-height) + var(--spacing));
    }
</style>
