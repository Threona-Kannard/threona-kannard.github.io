<script lang="ts">
    import { _, json } from "svelte-i18n";
    import Separator from "$lib/components/Separator.svelte";
    import Project from "$lib/components/projects/Project.svelte";
    import SparxImg from "/src/lib/assets/images/experiences/sparx.png?enhanced";
    import GarenaImg from "/src/lib/assets/images/experiences/garena.png?enhanced";
    import GameloftImg from "/src/lib/assets/images/experiences/gameloft.png?enhanced";

    const exp: any = $json("page.experience.experiences");
</script>

<svelte:head>
    <title>{$_("page.experience.title")}</title>
</svelte:head>

<h1 class="title">{$_("page.experience.title")}</h1>

<Separator />

<div class="project-list scroll">
    {#each exp as e}
        <div class="timeline-item">
            <div class="timeline-dot">
                {#if e.icon === "sparx"}
                    <enhanced:img
                        src={SparxImg}
                        alt="Sparx icon"
                        loading="lazy"
                        style={e.style}
                    />
                {:else if e.icon === "garena"}
                    <enhanced:img
                        src={GarenaImg}
                        alt="Garena icon"
                        loading="lazy"
                        style={e.style}
                    />
                {:else if e.icon === "gameloft"}
                    <enhanced:img
                        src={GameloftImg}
                        alt="Gameloft icon"
                        loading="lazy"
                        style={e.style}
                    />
                {/if}
            </div>
            <div class="timeline-body">
                <div class="timeline-title">{e.title}</div>
                <b class="hr anim"></b>
                <div class="timeline-company">🏰 {e.company}</div>
                <div class="timeline-date">📅 {e.date}</div>
                <div class="timeline-desc">{@html $_(e.desc)}</div>
                <div class="project-tags">
                    {#each e.tags as tag}
                        <dir class={`project-tag tag-${tag.toLowerCase()}`}>
                            <p>{tag}</p>
                        </dir>
                    {/each}
                </div>
            </div>
        </div>
    {/each}
</div>

<style lang="scss">
    $barsize: 15px;
    .hr {
        width: 63vw;
        height: 1px;
        display: block;
        position: relative;
        margin-bottom: 0em;
        padding: 3px 0;

        &:after,
        &:before {
            content: "";
            position: absolute;

            width: 100%;
            height: 1px;
            bottom: 50%;
            left: 0;
        }

        &:before {
            background: linear-gradient(
                90deg,
                var(--color-bg) 0%,
                var(--color-bg) 50%,
                transparent 50%,
                transparent 100%
            );
            background-size: $barsize;
            background-position: center;
            z-index: 1;
        }

        &:after {
            transition:
                opacity 0.3s ease,
                animation 0.3s ease;

            background: linear-gradient(
                to right,
                var(--color-cream) 0%,
                var(--color-accent) 20%,
                var(--color-warning) 40%,
                var(--color-blue-retro) 60%,
                var(--color-border) 80%,
                var(--color-fg) 100%
            );

            background-size: 200%;
            background-position: 0%;
            animation: bar 15s linear infinite;
        }

        @keyframes bar {
            0% {
                background-position: 0%;
            }
            100% {
                background-position: 200%;
            }
        }
    }

    .hr.anim {
        &:before {
            background: linear-gradient(
                90deg,
                var(--color-bg) 0%,
                var(--color-bg) 5%,
                transparent 5%,
                transparent 10%,
                var(--color-bg) 10%,
                var(--color-bg) 15%,
                transparent 15%,
                transparent 20%,
                var(--color-bg) 20%,
                var(--color-bg) 25%,
                transparent 25%,
                transparent 30%,
                var(--color-bg) 30%,
                var(--color-bg) 35%,
                transparent 35%,
                transparent 40%,
                var(--color-bg) 40%,
                var(--color-bg) 45%,
                transparent 45%,
                transparent 50%,
                var(--color-bg) 50%,
                var(--color-bg) 55%,
                transparent 55%,
                transparent 60%,
                var(--color-bg) 60%,
                var(--color-bg) 65%,
                transparent 65%,
                transparent 70%,
                var(--color-bg) 70%,
                var(--color-bg) 75%,
                transparent 75%,
                transparent 80%,
                var(--color-bg) 80%,
                var(--color-bg) 85%,
                transparent 85%,
                transparent 90%,
                var(--color-bg) 90%,
                var(--color-bg) 95%,
                transparent 95%,
                transparent 100%
            );

            background-size: $barsize * 10;
            background-position: center;
            z-index: 1;

            animation: bar 120s linear infinite;
        }
    }
    .project-list {
        display: flex;
        flex-direction: column;
        padding: var(--padding-m);
        gap: var(--padding-m);
        overflow-y: auto;
        max-height: 60vh;
        max-width: 70vw;
        margin-left: 2vw;
    }

    .timeline-item {
        display: flex;
        gap: 30px;
        padding: 10px;
        margin-bottom: 50px;
        margin-left: 10px;
        position: relative;

        .timeline-body {
            background: linear-gradient(to bottom, var(--color-blue-retro))
                center no-repeat;
            background-position: 0px 1000px;
            // border-bottom: var(--border-width) solid transparent;
            // border-top: var(--border-width) solid transparent;
            text-decoration: none;
            transition: 0.2s cubic-bezier(0, 1.8, 1, -1.51);
        }

        &:hover {
            .timeline-dot {
                background: color-mix(
                    in srgb,
                    var(--color-cream) 50%,
                    transparent
                );
                box-shadow: 0 0 30px var(--color-cream);
            }
            .timeline-body {
                background-position: 0px 0px;
                box-shadow: 0 0 20px 15px var(--color-blue-retro);
                // border-bottom: var(--border-width) solid var(--color-blue-retro);
            }

            .hr.anim {
                &:before {
                    animation-duration: 20s;
                }
                &:after {
                    animation-duration: 2s;
                }
            }
        }
    }
    .timeline-item::before {
        content: "";
        position: absolute;
        left: 46px;
        top: 85px;
        bottom: -45px;
        width: 3px;
        background: linear-gradient(180deg, var(--color-border), transparent);
    }
    .timeline-item:last-child::before {
        display: none;
    }

    .timeline-dot {
        width: 75px;
        height: 75px;
        border: 2px solid var(--color-border);
        background: color-mix(in srgb, var(--color-cream) 25%, transparent);
        border-radius: 50%;
        display: flex;
        align-items: center;
        justify-content: center;
        flex-shrink: 0;
        box-shadow: 0 0 22px var(--color-cream);
    }
    .timeline-title {
        font-family: "Orbitron", monospace;
        font-weight: bold;
        font-size: 28px;
        color: var(--color-cream);
        margin-bottom: 3px;
    }
    .timeline-company {
        font-size: 22px;
        color: var(--color-accent);
        margin-bottom: 3px;
    }
    .timeline-date {
        font-size: 16px;
        color: var(--color-border);
        margin-bottom: 7px;
    }
    .timeline-desc {
        font-size: 15px;
        color: var(--color-fg);
        line-height: 1.5;
    }

    :root {
        --tag-cpp-bg: #2b4b75be;
        --tag-cpp-border: #00599c;
        --tag-csharp-bg: #522b75be;
        --tag-csharp-border: #68217a;
        --tag-lua-bg: #2b3b75be;
        --tag-lua-border: #000080;
        --tag-docker-bg: #2b5f75be;
        --tag-docker-border: #2c6cbe;
        --tag-java-bg: #75492bbe;
        --tag-java-border: #76562c;
        --tag-git-bg: #75332bbe;
        --tag-git-border: #f05032;
        --tag-mongodb-bg: #2f752bbe;
        --tag-mongodb-border: #40762c;
        --tag-kotlin-bg: #612b75be;
        --tag-kotlin-border: #6c2cbe;
        --tag-react-bg: #362b75be;
        --tag-react-border: #3c2cbe;
        --tag-rust-bg: #75412bbe;
        --tag-rust-border: #76462c;
        --tag-scratch-bg: #f9a825be;
        --tag-scratch-border: #4d97ff;
        --tag-android-bg: #2b7549be;
        --tag-android-border: #3ddc84;
        --tag-typescript-bg: #2b4275be;
        --tag-typescript-border: #2c42be;
        --tag-javascript-bg: #756a2bbe;
        --tag-javascript-border: #f7df1e;
        --tag-perforce-bg: #4a2b75be;
        --tag-perforce-border: #6b00d7;
        --tag-python-bg: #2b4675be;
        --tag-python-border: #306998;
        --tag-unreal-bg: #4a4a4abe;
        --tag-unreal-border: #7d7d7d;
        --tag-unity-bg: #35383abe;
        --tag-unity-border: #80888f;
        --tag-jenkins-bg: #752b2bbe;
        --tag-jenkins-border: #d24939;
    }

    .project-tags {
        grid-area: 2 / 1 / 3 / 3;

        display: flex;
        flex-direction: row;
        flex-wrap: wrap;
        gap: var(--padding-s);
        margin-top: 15px;
    }

    .project-tag {
        height: fit-content;
        padding: 0.1rem 0.5rem;
        background-color: var(--tag-bg);
        border-radius: 0.75rem;
        border: solid var(--border-width) var(--tag-border);
    }

    /* TAG COLORS :3 */
    .tag-cpp {
        background-color: var(--tag-cpp-bg);
        border-color: var(--tag-cpp-border);
    }
    .tag-csharp {
        background-color: var(--tag-csharp-bg);
        border-color: var(--tag-csharp-border);
    }
    .tag-docker {
        background-color: var(--tag-docker-bg);
        border-color: var(--tag-docker-border);
    }
    .tag-java {
        background-color: var(--tag-java-bg);
        border-color: var(--tag-java-border);
    }
    .tag-mongodb {
        background-color: var(--tag-mongodb-bg);
        border-color: var(--tag-mongodb-border);
    }
    .tag-kotlin {
        background-color: var(--tag-kotlin-bg);
        border-color: var(--tag-kotlin-border);
    }
    .tag-react {
        background-color: var(--tag-react-bg);
        border-color: var(--tag-react-border);
    }
    .tag-lua {
        background-color: var(--tag-lua-bg);
        border-color: var(--tag-lua-border);
    }
    .tag-rust {
        background-color: var(--tag-rust-bg);
        border-color: var(--tag-rust-border);
    }
    .tag-scratch {
        background-color: var(--tag-scratch-bg);
        border-color: var(--tag-scratch-border);
    }
    .tag-android {
        background-color: var(--tag-android-bg);
        border-color: var(--tag-android-border);
    }
    .tag-typescript {
        background-color: var(--tag-typescript-bg);
        border-color: var(--tag-typescript-border);
    }
    .tag-javascript {
        background-color: var(--tag-javascript-bg);
        border-color: var(--tag-javascript-border);
    }
    .tag-git {
        background-color: var(--tag-git-bg);
        border-color: var(--tag-git-border);
    }
    .tag-perforce {
        background-color: var(--tag-perforce-bg);
        border-color: var(--tag-perforce-border);
    }
    .tag-python {
        background-color: var(--tag-python-bg);
        border-color: var(--tag-python-border);
    }
    .tag-unreal {
        background-color: var(--tag-unreal-bg);
        border-color: var(--tag-unreal-border);
    }
    .tag-unity {
        background-color: var(--tag-unity-bg);
        border-color: var(--tag-unity-border);
    }
    .tag-jenkins {
        background-color: var(--tag-jenkins-bg);
        border-color: var(--tag-jenkins-border);
    }

    .scroll {
        overflow: scroll;
        overflow-x: hidden;
        overflow-y: auto;

        /* Width of the scroll bar */
        &::-webkit-scrollbar {
            width: 10px;
        }

        /* Track (background) */
        &::-webkit-scrollbar-track {
            background-color: transparent;
        }

        /* Thumb (the moving part) */
        &::-webkit-scrollbar-thumb {
            background-color: transparent;
        }

        &:hover {
            &::-webkit-scrollbar-thumb {
                background: var(--color-cream);
                border-radius: 6px;
            }
            &::-webkit-scrollbar-track {
                background-color: var(--color-border);
                border: 2px solid var(--color-dark);
                border-radius: 6px;
            }

            /* On hover */
            &::-webkit-scrollbar-thumb:active {
                background: var(--color-accent);
            }
            &::-webkit-scrollbar-track:active {
                background: var(--color-blue-retro);
            }
        }
    }
</style>
