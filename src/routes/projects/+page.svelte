<script lang="ts">
    import { goto } from "$app/navigation";
    import { _, json } from "svelte-i18n";
    import { onMount } from "svelte";
    import Separator from "$lib/components/Separator.svelte";
    import Project from "$lib/components/projects/Project.svelte";
    // Images
    import LOLImg from "$lib/assets/images/projects/LOL/LOL.jpg?enhanced";
    import HaloImg from "$lib/assets/images/projects/HALO/HALO.jpg?enhanced";
    import NBAImg from "$lib/assets/images/projects/NBA/NBA.jpg?enhanced";

    type SlideMeta = {
        title?: string;
        link?: string;
        youtubeUrl?: string;
    };

    type ExternalProjectMeta = {
        title?: string;
        url?: string;
    };

    type ProjectData = {
        title: string;
        desc: string;
        image: string;
        tags: string[];
        images?: string[];
        imageTitles?: Record<number, SlideMeta> | Record<string, SlideMeta> | string[];
        externalUrl?: string | ExternalProjectMeta;
    };

    let showSparxOnly = $state(false);
    let showPersonalOnly = $state(false);
    let showTechArtOnly = $state(false);
    let showGameDevOnly = $state(false);
    let showAll = $state(true);

    const projectData = ($json("page.projects.projects") ??
        []) as ProjectData[];

    const projects: any = projectData.map((project) => {
        const externalLink =
            typeof project.externalUrl === "string"
                ? { title: "External project", url: project.externalUrl }
                : project.externalUrl ?? { title: "External project", url: "" };

        return {
            title: project.title,
            desc: project.desc,
            image: (() => {
                switch (project.image) {
                    case "LOL":
                        return LOLImg;
                    case "HALO":
                        return HaloImg;
                    case "NBA2k":
                        return NBAImg;
                    default:
                        return "";
                }
            })(),
            tags: project.tags,
            images: project.images ?? [],
            imageTitles: project.imageTitles ?? {},
            externalUrl: externalLink,
        };
    });

    const filterProjects = $derived.by(() => {
        const enabledFilters = [
            showSparxOnly && "Sparx*",
            showPersonalOnly && "Personal",
            showTechArtOnly && "TechArt",
            showGameDevOnly && "GameDev",
        ].filter(Boolean) as string[];

        if (showAll || enabledFilters.length === 0) {
            return projects;
        }

        return projects.filter((project: any) =>
            enabledFilters.every((filter) => project.tags.includes(filter))
        );
    });

    const projectAccordions = $derived.by(() => {
        const accordions: any[][] = [];

        for (let index = 0; index < filterProjects.length; index += 7) {
            accordions.push(filterProjects.slice(index, index + 7));
        }

        return accordions;
    });

    onMount(() => {
        const filterName = new URLSearchParams(window.location.search).get(
            "filter"
        );
        if (filterName) {
            document
                .querySelector<HTMLButtonElement>(
                    `button[name="${filterName}"]`
                )
                ?.click();
        }

        const handleResponsive = () => {
            if (window.innerWidth <= 700) {
                document
                    .querySelectorAll<HTMLElement>(".accordion-section")
                    .forEach((section) => {
                        section.addEventListener("click", () => {
                            document
                                .querySelectorAll<HTMLElement>(
                                    ".accordion-section"
                                )
                                .forEach((s) => {
                                    s.setAttribute("style", "flex: 1;");
                                    if (s !== section) {
                                        s?.querySelector(
                                            ".section-content"
                                        )?.setAttribute("style", "opacity: 0;");
                                    }
                                });
                            section.setAttribute("style", "flex: 6;");
                        });
                    });
            }
        };

        handleResponsive();
        window.addEventListener("resize", handleResponsive);

        return () => {
            window.removeEventListener("resize", handleResponsive);
        };
    });

    const handleFilter = (event: Event) => {
        const button = event.currentTarget as HTMLButtonElement;

        if (button.name === "all") {
            showAll = true;
            showSparxOnly = false;
            showPersonalOnly = false;
            showTechArtOnly = false;
            showGameDevOnly = false;
            document
                .querySelectorAll<HTMLButtonElement>(".filter-btn")
                .forEach((filterButton) =>
                    filterButton.classList.toggle(
                        "active",
                        filterButton.name === "all"
                    )
                );
            return;
        }

        button.classList.toggle("active");
        showAll = false;
        document
            .querySelector<HTMLButtonElement>('button[name="all"]')
            ?.classList.remove("active");

        if (button.name === "sparx") {
            showSparxOnly = button.classList.contains("active") ? true : false;
            if (showSparxOnly) {
                showPersonalOnly = false;
                document
                    .querySelector<HTMLButtonElement>('button[name="personal"]')
                    ?.classList.remove("active");
            }
            console.log("showSparxOnly:", showSparxOnly);
        }
        if (button.name === "personal") {
            showPersonalOnly = button.classList.contains("active")
                ? true
                : false;
            if (showPersonalOnly) {
                showSparxOnly = false;
                document
                    .querySelector<HTMLButtonElement>('button[name="sparx"]')
                    ?.classList.remove("active");
            }
            console.log("showPersonalOnly:", showPersonalOnly);
        }
        if (button.name === "techart") {
            showTechArtOnly = button.classList.contains("active")
                ? true
                : false;
            console.log("showTechArtOnly:", showTechArtOnly);
        }
        if (button.name === "gamedev") {
            showGameDevOnly = button.classList.contains("active")
                ? true
                : false;
            console.log("showGameDevOnly:", showGameDevOnly);
        }

        if (
            !showSparxOnly &&
            !showPersonalOnly &&
            !showTechArtOnly &&
            !showGameDevOnly
        ) {
            showAll = true;
            document
                .querySelector<HTMLButtonElement>('button[name="all"]')
                ?.classList.add("active");
        }
    };
</script>

<svelte:head>
    <title>{$_("page.projects.title")}</title>
</svelte:head>

<div class="page-header">
    <button class="back-button" onclick={() => goto("/")}>← Back to home</button
    >
    <h1 class="title">{$_("page.projects.title")}</h1>
</div>

<Separator margin={false} />

<div class="portfolio-container">
    <div class="header-container">
        <h1>Filters:</h1>
        <div class="filter-btns">
            <button class="filter-btn active" onclick={handleFilter} name="all"
                >All</button
            >
            <button class="filter-btn" onclick={handleFilter} name="sparx"
                >Sparx*</button
            >
            <button class="filter-btn" onclick={handleFilter} name="techart"
                >TechArt</button
            >
            <button class="filter-btn" onclick={handleFilter} name="gamedev"
                >GameDev</button
            >
            <button class="filter-btn" onclick={handleFilter} name="personal"
                >Personal</button
            >
        </div>
    </div>
    <div class="accordion-container {projectData.length > 7 ? "scroll" : "no-scroll"}">
        {#each projectAccordions as accordionProjects}
            <div class="accordion">
                {#each accordionProjects as project}
                    <Project
                        name={project.title}
                        description={project.desc}
                        img={project.image}
                        tags={project.tags}
                        images={project.images}
                        imageTitles={project.imageTitles}
                        externalUrl={project.externalUrl}
                    ></Project>
                {/each}
            </div>
        {/each}
    </div>
</div>

<style>
    :root {
        --bg-color: #0f0f0f;
        --text-color: #e6e6e6;
        --accent-color: #2a2a2a;
        --hover-color: #363636;
        --highlight-color: #525252;
        --fontSize: 18px;
    }
    .portfolio-container {
        margin-top: -1rem;
        width: 75vw;
        height: 625px;
        display: flex;
        flex-direction: column;
        overflow: hidden;
        position: relative;

        &:has(*:hover) {
            .header-container h1::after {
                width: 150%;
            }
        }
    }

    .page-header {
        display: flex;
        flex-wrap: wrap;
        gap: var(--padding-s);
        align-items: center;
        justify-content: space-between;
    }

    .header-container {
        padding: 1rem 0;
        text-align: left;
        position: relative;
        z-index: 10;
    }

    .header-container h1 {
        font-size: 1.8rem;
        font-weight: 700;
        letter-spacing: -0.03em;
        margin-bottom: 0.5rem;
        position: relative;
        display: inline-block;
    }

    .header-container h1::after {
        content: "";
        position: absolute;
        width: 150px;
        height: 3px;
        background-color: var(--highlight-color);
        bottom: -8px;
        left: 0;
        /* transform: translateX(-50%); */
        transition: width 0.5s ease;
    }

    .filter-btns {
        text-align: left;
        width: 100%;
        white-space: nowrap;
        margin-top: 1.5rem;
        padding-left: 0.5rem;
    }

    .filter-btn {
        font-size: var(--fontSize);
        font-family: "departure-mono", monospace;
        font-weight: bold;
        position: relative;
        z-index: 1;
        margin: 0 calc(var(--fontSize) * 0.25);
        background: transparent;
        display: inline-block;
        border-radius: 20px;
        border: none;
        color: var(--color-fg);
        border: 3px solid var(--color-border);
        padding: calc(var(--fontSize) * 0.8) calc(var(--fontSize) * 1.6);
        cursor: pointer;
        appearance: none;
        transition: all 0.2s ease-out;

        &:hover {
            box-shadow: 0 0 12px 3px var(--color-accent);
        }

        &:global(.active) {
            background: var(--color-warning);
            border: 3px solid var(--color-border);

            &:hover {
                background: var(--color-blue);
                box-shadow: none;
            }
        }
    }

    .filter-btn:before {
        content: "";
        position: absolute;
        height: 100%;
        left: calc(var(--fontSize) * 0.7);
        top: 0;
        width: 1px;
        background: var(--color-fg);
        transform: scaleY(0);
        transition: transform 0.2s ease-in-out;
    }

    :global(.filter-btn.active + .filter-btn.active) {
        border-radius: 0 20px 20px 0;
        margin-left: calc(var(--fontSize) * -2);
        padding-left: 1em;
        border-left: none;
    }
    :global(.filter-btn.active + .filter-btn.active:before) {
        transform: scaleY(0);
    }

    .accordion {
        display: flex;
        width: 100%;
        height: 460px;
        margin-top: 1rem;
    }

    .accordion + .accordion {
        margin-top: -5rem;
    }

    .accordion-container {
        display: flex;
        flex-direction: column;
        overflow-y: auto;
        max-height: 60vh;
        max-width: 100vw;
        gap: 50px;

        &.no-scroll {
            overflow: hidden;
        }
    }

    .portfolio-container:has(.accordion + .accordion) {
        height: auto;
        overflow: visible;
    }

    .back-button {
        appearance: none;
        background: transparent;
        border: 1px solid var(--color-border);
        color: var(--color-fg);
        padding: 0.75rem 1rem;
        border-radius: var(--border-radius);
        cursor: pointer;
        transition:
            background-color 0.2s ease,
            color 0.2s ease;
    }

    .back-button:hover {
        background-color: var(--color-fg);
        color: var(--color-bg);
    }

    @media (max-width: 700px) {
        .portfolio-container {
            width: 100%;
            height: auto;
        }

        .accordion {
            flex-direction: column;
            height: auto;
        }

        .header-container h1 {
            font-size: 1.5rem;
        }
    }
</style>
