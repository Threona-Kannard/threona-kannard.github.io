<script lang="ts">
    import { _ } from "svelte-i18n";
    import { onMount } from "svelte";
    import Separator from "$lib/components/Separator.svelte";
    import Project from "$lib/components/projects/Project.svelte";
    // Images
    import Rubiu5Img from "$lib/assets/images/projects/rubiu5.webp?enhanced";
    import ArchanImg from "$lib/assets/images/projects/archan.webp?enhanced";
    import StarMCImg from "$lib/assets/images/projects/starmc.webp?enhanced";
    import DnDAbenyuImg from "$lib/assets/images/projects/dnd_abenyu.webp?enhanced";
    import RyokoImg from "$lib/assets/images/projects/ryoko.webp?enhanced";

    let showSparxOnly = false;

    onMount(() => {

        const handleResponsive = () => {
            if (window.innerWidth <= 700) {
                document.querySelectorAll<HTMLElement>(".accordion-section").forEach((section) => {
                    section.addEventListener("click", () => {
                        document.querySelectorAll<HTMLElement>(".accordion-section").forEach((s) => {
                            s.setAttribute("style", "flex: 1;");
                            if (s !== section) {
                                s?.querySelector(".section-content")?.setAttribute("style", "opacity: 0;");
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
        const checkbox = event.target as HTMLInputElement;
        showSparxOnly = checkbox.checked;
    };
</script>

<svelte:head>
    <title>{$_("page.projects.title")}</title>
</svelte:head>

<h1 class="title">{$_("page.projects.title")}</h1>

<Separator />

<div class="portfolio-container">
    <div class="header-container">
        <h1>Sparx* - a Virtuos Studio</h1>
        <p>
            A collection of my personal and collaborative projects, showcasing
            my skills in design, development, and creative problem-solving.
        </p>
        <input class="filter" placeholder="Sparx*" type="checkbox" onchange={handleFilter}/>
    </div>
    <div class="accordion">
        <Project
            name="Rubiu5"
            description="A collaborative project with Rubiu5, focusing on innovative web design and interactive experiences."
            img={Rubiu5Img}
            tags={["Web Design", "Collaboration", "Interactive", "Sparx*"]}>
        </Project>
        <Project
            name="Archan"
            description="A solo project exploring the intersection of architecture and digital media."
            img={ArchanImg}
            tags={["Architecture", "Digital Media", "Exploration", "Sparx*"]}>
        </Project>
        <Project
            name="StarMC"
            description="A Minecraft-inspired game development project with a focus on community building."
            img={StarMCImg}
            tags={["Game Development", "Community", "Minecraft"]}>
        </Project>
        <Project
            name="DnD Abenyu"
            description="A tabletop RPG campaign set in the world of Abenyu, featuring custom character classes and magic systems."
            img={DnDAbenyuImg}
            tags={["Tabletop RPG", "Worldbuilding", "Character Design", "Sparx*"]}>
        </Project>
        <Project
            name="Ryoko"
            description="A personal branding project for a creative professional, emphasizing minimalism and functionality."
            img={RyokoImg}
            tags={["Branding", "Identity", "Minimalism"]}>
        </Project>
    </div>
</div>

<style>
    :root {
        --bg-color: #0f0f0f;
        --text-color: #e6e6e6;
        --accent-color: #2a2a2a;
        --hover-color: #363636;
        --highlight-color: #525252;
    }
    .portfolio-container {
        width: 75vw;
        height: 625px;
        display: flex;
        flex-direction: column;
        overflow: hidden;
        position: relative;

        &:has(*:hover){
            .header-container h1::after {
                width: 150%;
            }
        }
    }

    .header-container {
        padding: 1.5rem 0;
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

    .header-container p {
        font-size: 0.85rem;
        opacity: 0.7;
        max-width: 80%;
        margin: 1rem 0 0;
        line-height: 1.5;
    }

    .accordion {
        display: flex;
        width: 100%;
        height: 460px;
        margin-top: 1rem;
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
