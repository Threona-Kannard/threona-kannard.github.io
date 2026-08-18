<script lang="ts">
    import { _, json } from "svelte-i18n";
    import SparxImg from "/src/lib/assets/images/experiences/sparx.png?enhanced";
    import GarenaImg from "/src/lib/assets/images/experiences/garena.png?enhanced";
    import GameloftImg from "/src/lib/assets/images/experiences/gameloft.png?enhanced";

    const e: any = $json("page.experience.experiences");
</script>

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
        <div class="experience-tags">
            {#each e.tags as tag}
                <div class={`experience-tag tag-${tag.toLowerCase()}`}>
                    <p>{tag}</p>
                </div>
            {/each}
        </div>
        {#if e.hasProject}
            <button
                class="experience-link"
                onclick={() =>
                    window.open(`/projects?filter=${e.icon}`, "_self")}
                title="View Project"
            >
                <svg
                    class="experience-nav"
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
            </button>
        {/if}
    </div>
</div>

<style lang="scss">
    $barsize: 15px;

    .experience-link {
        position: absolute;
        right: 0;
        bottom: 0;
        margin: var(--padding-s);
        background-color: transparent;
        border: none;
        cursor: pointer;

        &:hover {
            .experience-nav {
                fill: var(--color-accent);
            }
        }
    }

    .experience-nav {
        height: 2rem;
        width: 2rem;
        top: 0;
        animation: experienceArrow 2s ease infinite;
    }

    /* ANIMATIONS */
    @keyframes experienceArrow {
        0%,
        100% {
            margin-right: 0rem;
        }
        50% {
            margin-right: 1rem;
        }
    }

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

    .experience-list {
        display: flex;
        flex-direction: column;
        padding: var(--padding-m);
        gap: var(--padding-m);
        overflow-y: auto;
        max-height: 70vh;
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
    }
</style>
