<script lang="ts">
    import { _, json } from "svelte-i18n";
    import WavyText from "$lib/components/WavyText.svelte";
    import Separator from "$lib/components/Separator.svelte";
    import Spells from "$lib/components/index/Spells.svelte";
    import Card from "$lib/components/index/Card.svelte";
    // Images
    import ThreonaGitImg from "$lib/assets/images/threona-github.png?enhanced";

    const messages = ($json("page.home.greeting") as string[] | null) ?? [];
    let currentMessage = $state(0);

    function randomMessage() {
        currentMessage = Math.floor(Math.random() * messages.length);
        if (currentMessage === 0) randomMessage();
    }
</script>

<svelte:head>
    <title>Threona's Workspace</title>
</svelte:head>

<h1 class="title">
    <WavyText text="Threona's Workspace" />
</h1>

<Separator />

<div class="container">
    <div class="character-container">
        <div class="character-dialog-container">
            <enhanced:img
                class="character-img"
                src={ThreonaGitImg}
                alt="Profile of Threona on Github"
                loading="lazy"
            />

            {#key messages[currentMessage]}
                <!-- svelte-ignore a11y_click_events_have_key_events -->
                <!-- svelte-ignore a11y_no_static_element_interactions -->
                <div class="character-dialog" onclick={() => randomMessage()}>
                    <!-- Connector for the speech balloon -->
                    <svg
                        class="character-dialog-connector"
                        viewBox="0 0 32 32"
                        xmlns="http://www.w3.org/2000/svg"
                        ><path d="M20.697 24L9.303 16.003 20.697 8z" /></svg
                    >

                    <div class="character-dialog__name-container">
                        <h3 class="text-3xl font-bold border-b-4">Threona:</h3>

                        <svg
                            class="character-dialog__next"
                            fill="var(--color-fg)"
                            width="2rem"
                            height="2rem"
                            viewBox="0 0 12 20"
                            version="1.1"
                            xmlns="http://www.w3.org/2000/svg"
                            ><path
                                d="m 12.000001,8 v 4 H 8 v 4 H 4 v 4 H 0 V 0 h 4 v 4 h 4 v 4 z"
                            /></svg
                        >
                    </div>

                    <div class="character-dialog__text">
                        <WavyText
                            text={messages[currentMessage]}
                            fadeIn={true}
                            delay={0.02}
                        />
                    </div>
                </div>
            {/key}
        </div>

        <div class="character-spells-container">
            <Spells maxSlots={5} usedSlots={5} level={5} />
            <Spells maxSlots={3} usedSlots={1} level={2} />
            <Spells maxSlots={4} usedSlots={2} level={3} />
        </div>
    </div>

    <div class="vim-title">
        <p>Main Hub</p>
        <p>{"[1:1]"}</p>
        <p>Done</p>
    </div>
    <div class="cards-container">
        <Card
            icon={"<path d='M16 15a1 1 0 0 1-2 0V8A6 6 0 1 0 2 8v7a1 1 0 0 1-2 0V8a8 8 0 1 1 16 0v7zm-4-3a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1zm-4 0a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1zm-4 0a1 1 0 0 1 1 1v2a1 1 0 0 1-2 0v-2a1 1 0 0 1 1-1zm2-6a1 1 0 1 1 0 2 1 1 0 0 1 0-2zm4 0a1 1 0 1 1 0 2 1 1 0 0 1 0-2z' fill-rule='evenodd'/>"}
            name={$_("page.home.links.about")}
            link={"/about"}
            newtab={false}
        />
        <Card
            icon={"<path d='M8 8v5h4V8h-2V6H8v2zm-8 8h16V0H0v16zm2-2V2h12v12H2zM8 4h2V2H8v2zm2 2h2V4h-2v2zm-1 6v-2h2v2H9z' fill-rule='evenodd'/>"}
            name={$_("page.home.links.projects")}
            link={"/projects"}
            newtab={false}
        />
    </div>

    <div class="vim-title">
        <p>Artworks and Showcases</p>
        <p>{"[1:2]"}</p>
        <p>Done</p>
    </div>

    <div class="cards-container">
        <Card
            icon={"<path d='M1033.05,324.45c-0.19-137.9-107.59-250.92-233.6-291.7c-156.48-50.64-362.86-43.3-512.28,27.2 C106.07,145.41,49.18,332.61,47.06,519.31c-1.74,153.5,13.58,557.79,241.62,560.67c169.44,2.15,194.67-216.18,273.07-321.33 c55.78-74.81,127.6-95.94,216.01-117.82C929.71,603.22,1033.27,483.3,1033.05,324.45z'/>"}
            name={$_("page.home.links.patreon")}
            link={"https://patreon.com/threona_techart"}
            newtab={true}
            x={1088}
            y={1088}
        />
        <Card
            icon={"<path d='M0 23.63l2.703 4.672c0.552 1.094 1.667 1.781 2.885 1.781h17.943l-3.724-6.453zM32 23.661c0-0.641-0.193-1.245-0.516-1.75l-10.516-18.276c-0.557-1.057-1.656-1.719-2.854-1.719h-5.557l16.24 28.135 2.563-4.432c0.5-0.849 0.641-1.224 0.641-1.958zM17.161 19.047l-7.255-12.568-7.26 12.568z'/>"}
            name={$_("page.home.links.artstation")}
            link={"https://www.artstation.com/threonahuynh"}
            newtab={true}
            x={32}
            y={32}
        />
        <Card
            icon={"<path d='m 14.054544,2.4061821 c 0,0 -1.930909,-0.2429091 -6.0778174,-0.2429091 -4.0123632,0 -6.0319994,0.2429091 -6.0319994,0.2429091 A 1.9454544,1.9454544 0 0 0 2.3778175e-8,4.3516365 V 11.649091 A 1.9454544,1.9454544 0 0 0 1.9447272,13.595272 c 0,0 1.877818,0.241455 6.0319994,0.241455 4.1519994,0 6.0778174,-0.241455 6.0778174,-0.241455 a 1.9439999,1.9439999 0 0 0 1.945455,-1.946181 V 4.3501819 A 1.9439999,1.9439999 0 0 0 14.054544,2.4061821 Z M 5.8625451,10.890545 V 5.1123637 l 5.1883629,2.8872725 z' style='stroke-width:0.727273'/>"}
            name={$_("page.home.links.youtube")}
            link={"https://www.youtube.com/@threona.techart"}
            newtab={true}
        />
    </div>

    <div class="vim-title">
        <p>Contact</p>
        <p>{"[1:3]"}</p>
        <p>Done</p>
    </div>
    <div class="cards-container">
        <Card
            icon={"<path d='M 0,0 H 16 V 12 H 4 V 4 h 8 v 6 h 2 V 2 H 2 v 12 h 14 v 2 H 0 Z M 10,10 V 6 H 6 v 4 z'/>"}
            name={$_("page.home.links.contact")}
            link={"/contact"}
            newtab={false}
        />
        <Card
            icon={"<path d='M 15.921648,5.9648307 C 15.405668,3.2409386 12.681776,2.902452 12.681776,2.902452 H 0.48225919 c -0.40398399,0 -0.45348203,0.531479 -0.45348203,0.531479 0,0 -0.05449784,4.8833065 -0.01349947,7.883188 0.10999565,1.613936 1.72393171,1.780429 1.72393171,1.780429 0,0 5.5102818,-0.0155 7.9761842,-0.0335 1.6254354,-0.283987 1.7894294,-1.711431 1.7704304,-2.4899 2.903885,0.161494 4.947804,-1.8879251 4.435324,-4.6093173 z M 8.5464399,8.3062379 C 7.7159728,9.2721997 5.8725458,10.954633 5.8725458,10.954633 c 0,0 -0.080497,0.0805 -0.2084918,0.0155 -0.049498,-0.0365 -0.069997,-0.06 -0.069997,-0.06 C 5.2965686,10.616146 3.3486457,8.8787153 2.9036633,8.2747392 2.432182,7.6312647 2.2111907,6.4753105 2.8441656,5.8008372 3.4766406,5.1288638 4.8465863,5.0768659 5.7525505,6.0713265 c 0,0 1.0414588,-1.187453 2.3124084,-0.6404747 1.2679498,0.5474784 1.2214517,2.0079205 0.481481,2.8753861 z m 4.1148371,0.3179875 c -0.619975,0.077997 -1.121956,0.017999 -1.121956,0.017999 v -3.78635 h 1.179454 c 0,0 1.315448,0.3674855 1.315448,1.7579304 0,1.2759494 -0.656474,1.7784295 -1.372446,2.0104204 z'/>"}
            name={$_("page.home.links.donate")}
            link={"https://ko-fi.com/threonahuynh"}
            newtab={true}
        />
    </div>
</div>

<style lang="postcss">
    @reference "tailwindcss";
    .container {
        display: flex;
        flex-direction: column;
        gap: var(--padding-x);
        margin: var(--padding-m) auto;
    }

    /* CHARACTER */
    .character-container {
        display: flex;
        justify-content: space-between;
        flex-wrap: nowrap;
        gap: var(--padding-m);
        margin-bottom: 2.5rem;
    }

    .character-dialog-container {
        display: grid;
        flex-wrap: wrap;
        grid-template-columns: 5rem auto;
        gap: var(--padding-x);
        cursor: default;
    }

    .character-img {
        width: 100%;
        height: auto;
    }

    .character-dialog {
        position: relative;
        width: fit-content;
        padding: var(--padding-m);
        border: var(--color-border) dashed var(--border-width);
    }

    .character-dialog__name-container {
        display: flex;
        justify-content: space-between;
    }
    .character-dialog__next {
        height: 1rem;
        width: 1rem;
        top: 0;
        animation: messageArrow 2s ease infinite;
    }

    .character-dialog__text {
        margin-top: var(--padding-m);
        font-size: clamp(1rem, 3vw, 1.5rem);
    }

    .character-dialog-connector {
        position: absolute;
        left: -1.1rem;
        height: 1.7rem;
        fill: var(--color-border);
    }

    .character-spells-container {
        display: flex;
        flex-direction: column;
        align-items: end;
        justify-content: center;
        gap: var(--padding-s);
        margin-left: auto;
        font-weight: bold;
        font-size: clamp(1rem, 2vw, 1.2rem);
    }

    /* SOCIALS */
    .vim-title {
        width: 100%;
        display: grid;
        grid-template-columns: 1fr 15% min-content;
        background-color: var(--color-border);
        font-size: clamp(1rem, 2vw, 1.2rem);
        font-weight: bold;
    }
    .vim-title p {
        color: var(--color-fg);
        padding: 0 var(--padding-s);
    }

    /* CARDS */
    .cards-container {
        display: grid;
        grid-template-columns: 1fr 1fr 1fr;
        gap: var(--padding-m);
    }

    /* ANIMATIONS */
    @keyframes messageArrow {
        0%,
        100% {
            margin-right: 0rem;
        }
        50% {
            margin-right: 1rem;
        }
    }

    /* RESPONSIVE */
    @media screen and (max-width: 728px) {
        .character-container {
            flex-direction: column;
        }
        .character-spells-container {
            width: 100%;
            align-items: unset;
            margin-left: unset;
        }

        .cards-container {
            grid-template-columns: 1fr;
        }
    }
</style>
