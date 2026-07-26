<script lang="ts">
    // Images
    import RustImg from "$lib/assets/images/tools/rust.webp?enhanced";
    import CppImg from "$lib/assets/images/tools/cpp.png";
    import CsharpImg from "$lib/assets/images/tools/csharp.png?enhanced";
    import VerseImg from "$lib/assets/images/tools/verse.png?enhanced";
    import DartImg from "$lib/assets/images/tools/dart.png?enhanced";
    import LuaImg from "$lib/assets/images/tools/lua.png?enhanced";
    import TypeScriptImg from "$lib/assets/images/tools/typescript.webp?enhanced";
    import JavaScriptImg from "$lib/assets/images/tools/javascript.webp?enhanced";
    import PythonImg from "$lib/assets/images/tools/python.webp?enhanced";
    import KotlinImg from "$lib/assets/images/tools/kotlin.png?enhanced";
    import JavaImg from "$lib/assets/images/tools/java.webp?enhanced";
    import GoImg from "$lib/assets/images/tools/golang.webp?enhanced";
    import BashImg from "$lib/assets/images/tools/bash.webp?enhanced";
    import SvelteImg from "$lib/assets/images/tools/svelte.png?enhanced";
    import NextJsImg from "$lib/assets/images/tools/nextjs.png?enhanced";
    import ReactImg from "$lib/assets/images/tools/react.png?enhanced";
    import BootstrapImg from "$lib/assets/images/tools/bootstrap.png?enhanced";
    import TailwindImg from "$lib/assets/images/tools/tailwind.png?enhanced";
    import PostgresImg from "$lib/assets/images/tools/postgres.webp?enhanced";
    import MondongoDBImg from "$lib/assets/images/tools/mondongodb.webp?enhanced";
    import SqliteImg from "$lib/assets/images/tools/sqlite.png?enhanced";
    import FlutterImg from "$lib/assets/images/tools/flutter.png?enhanced";
    import DjangoImg from "$lib/assets/images/tools/django.png?enhanced";
    import ExpressImg from "$lib/assets/images/tools/expressdotjs.png?enhanced";
    import NestImg from "$lib/assets/images/tools/nestjs.png?enhanced";
    import FirebaseImg from "$lib/assets/images/tools/firebase.png?enhanced";
    import Separator from "../Separator.svelte";
</script>

<div class="tools-container">
    <fieldset class="tools-section">
        <legend>Runes</legend>
        <fieldset class="tools-subsection">
            <legend>Core Runes</legend>
            <div title="Cpp" class="tool-entry">
                <enhanced:img src={CppImg} alt="" loading="lazy" />
            </div>

            <div title="Csharp" class="tool-entry">
                <enhanced:img src={CsharpImg} alt="" loading="lazy" />
            </div>

            <div title="Verse" class="tool-entry">
                <enhanced:img src={VerseImg} alt="" loading="lazy" />
            </div>

            <div title="Rust" class="tool-entry">
                <enhanced:img src={RustImg} alt="" loading="lazy" />
            </div>

            <div title="Go" class="tool-entry">
                <enhanced:img src={GoImg} alt="" loading="lazy" />
            </div>
        </fieldset>

        <Separator margin={false} />

        <fieldset class="tools-subsection">
            <legend>Realm Runes</legend>
            <div title="Kotlin" class="tool-entry">
                <enhanced:img src={KotlinImg} alt="" loading="lazy" />
            </div>

            <div title="Dart" class="tool-entry">
                <enhanced:img src={DartImg} alt="" loading="lazy" />
            </div>

            <div title="Java" class="tool-entry">
                <enhanced:img src={JavaImg} alt="" loading="lazy" />
            </div>
        </fieldset>

        <Separator margin={false} />
        <fieldset class="tools-subsection">
            <legend>Trickster Runes</legend>
            <div title="Python" class="tool-entry">
                <enhanced:img src={PythonImg} alt="" loading="lazy" />
            </div>

            <div title="Lua" class="tool-entry">
                <enhanced:img src={LuaImg} alt="" loading="lazy" />
            </div>

            <div title="TypeScript" class="tool-entry">
                <enhanced:img src={TypeScriptImg} alt="" loading="lazy" />
            </div>

            <div title="JavaScript" class="tool-entry">
                <enhanced:img src={JavaScriptImg} alt="" loading="lazy" />
            </div>

            <div title="Bash/Batch" class="tool-entry">
                <enhanced:img src={BashImg} alt="" loading="lazy" />
            </div>
        </fieldset>
    </fieldset>

    <fieldset class="tools-section">
        <legend>Grimoires</legend>

        <fieldset class="tools-subsection">
            <legend>Illusion Runes</legend>
            <div title="Svelte" class="tool-entry">
                <enhanced:img src={SvelteImg} alt="" loading="lazy" />
            </div>

            <div title="NextJS" class="tool-entry">
                <enhanced:img src={NextJsImg} alt="" loading="lazy" />
            </div>

            <div title="React" class="tool-entry">
                <enhanced:img src={ReactImg} alt="" loading="lazy" />
            </div>

            <div title="Bootstrap" class="tool-entry">
                <enhanced:img src={BootstrapImg} alt="" loading="lazy" />
            </div>

            <div title="Tailwind" class="tool-entry">
                <enhanced:img src={TailwindImg} alt="" loading="lazy" />
            </div>

            <div title="Flutter" class="tool-entry">
                <enhanced:img src={FlutterImg} alt="" loading="lazy" />
            </div>
        </fieldset>

        <Separator margin={false} />

        <fieldset class="tools-subsection">
            <legend>Underworld Grimoires</legend>

            <div title="ExpressJS" class="tool-entry">
                <enhanced:img src={ExpressImg} alt="" loading="lazy" />
            </div>

            <div title="NestJS" class="tool-entry">
                <enhanced:img src={NestImg} alt="" loading="lazy" />
            </div>

            <div title="Django" class="tool-entry">
                <enhanced:img src={DjangoImg} alt="" loading="lazy" />
            </div>
        </fieldset>
        <Separator margin={false} />

        <fieldset class="tools-subsection">
            <legend>Chronicle Grimoires</legend>

            <div title="Firebase" class="tool-entry">
                <enhanced:img src={FirebaseImg} alt="" loading="lazy" />
            </div>

            <div title="Postgres" class="tool-entry">
                <enhanced:img src={PostgresImg} alt="" loading="lazy" />
            </div>

            <div title="MondongoDB" class="tool-entry">
                <enhanced:img src={MondongoDBImg} alt="" loading="lazy" />
            </div>

            <div title="SQLite" class="tool-entry">
                <enhanced:img src={SqliteImg} alt="" loading="lazy" />
            </div>
        </fieldset>
    </fieldset>
</div>

<style>
    .tools-container {
        display: flex;
        gap: var(--padding-m);
    }

    .tools-section {
        display: flex;
        flex: 1;
        min-width: 0;
        flex-wrap: wrap;
        gap: var(--padding-s);
        border: var(--color-border) solid var(--border-width);
        padding: var(--padding-m);
    }

    .tools-subsection {
        display: flex;
        flex-wrap: nowrap;
        width: 100%;
        justify-content: space-evenly;
        gap: var(--padding-m);
        border: var(--color-border) solid var(--border-width);
        padding: var(--padding-m);
    }

    .tool-entry {
        height: 3rem;
    }
    .tool-entry img {
        height: 100%;
        width: auto;
    }
</style>
