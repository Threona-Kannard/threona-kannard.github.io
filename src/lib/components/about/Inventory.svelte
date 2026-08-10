<script lang="ts">
    import { goto } from "$app/navigation";
    import CameraImg from "$lib/assets/images/inventory/camera.png?enhanced";
    import PhoneImg from "$lib/assets/images/inventory/s23_ultra.png?enhanced";
    import RogAllyImg from "$lib/assets/images/inventory/rog_ally.png?enhanced";
    import DapImg from "$lib/assets/images/inventory/rg353ps.png?enhanced";
</script>

<div class="about-inventory">
    <button class="inventory-item one" onclick={() => goto("/galleries")}>
        <div class="image-wrapper">
            <enhanced:img src={CameraImg} alt="" loading="lazy"> </enhanced:img>
        </div>
        <p>Canon A3100 IS</p>
    </button>

    <button class="inventory-item two" onclick={() => goto("/music")}>
        <div class="image-wrapper">
            <enhanced:img src={PhoneImg} alt="" loading="lazy"> </enhanced:img>
        </div>
        <p>Samsung S23 Ultra</p>
    </button>

    <button class="inventory-item three" onclick={() => goto("/games")}>
        <div class="image-wrapper">
            <enhanced:img src={RogAllyImg} alt="" loading="lazy">
            </enhanced:img>
        </div>
        <p>ROG Ally</p>
    </button>

    <button class="inventory-item four" onclick={() => goto("/games/GameRetro")}>
        <div class="image-wrapper">
            <enhanced:img src={DapImg} alt="" loading="lazy"> </enhanced:img>
        </div>
        <p>Anbernic RG353PS</p>
    </button>
</div>

<style>
    .about-inventory {
        display: grid;

        /* Create 3 equal width columns (1 fr = 1 free fraction) */
        grid-template-columns: repeat(4, 1fr);

        /* Create 2 rows, for this example we set a container height */
        grid-template-rows: repeat(2, 200px);

        /* Define the layout area. Box 1 and 2 span across both rows */
        grid-template-areas:
            "area1 area2 area3 area3"
            "area4 area2 area3 area3";

        /* Add spacing (gutters) between boxes */
        gap: 75px;
    }

    .inventory-item {
        display: flex;
        flex-direction: column;
        justify-content: center; /* Center the number horizontally */
        align-items: center; /* Center the number vertically */
    }

    .image-wrapper {
        display: inline-block;
        position: relative;
        padding: 10px; /* Gives space for the glow to spread */
    }
    :global(.inventory-item img) {
        height: auto;
        min-width: 100%;
        image-rendering: pixelated;

        /* Crucial: Smoothly animates the filter change over 0.4 seconds */
        transition: filter 0.4s ease-out;

        /* Initial state: no shadow (optional, good practice) */
        filter: drop-shadow(0 0 0 transparent);
    }

    /* 3. The Hover State Trigger */
    :global(.image-wrapper:hover img) {
        /* 
       Synthesis of a Glow:
       drop-shadow(horizontal-offset vertical-offset blur-radius color)
       
       We use 0 offsets to make the glow symmetrical.
       We use rgba for ROG neon magenta: rgba(255, 0, 150, 0.9)
    */
        filter: drop-shadow(0 0 20px var(--color-cream));
    }

    /* Assign each HTML div to its defined grid area */
    .one {
        grid-area: area1;
    }
    .two {
        grid-area: area2;
    }
    .three {
        grid-area: area3;
    }
    .four {
        grid-area: area4;
    }

    /* RESPONSIVE */
    @media screen and (max-width: 728px) {
        .about-inventory {
            display: flex;
            flex-direction: column;
            gap: 0;
        }

        .inventory-item {
            display: flex;
            align-items: center;
            padding: var(--padding-s) 0;
        }
        .inventory-item:not(:last-child) {
            border-bottom: var(--border-width) solid var(--color-border);
        }
        :global(.inventory-item img) {
            height: auto;
            max-height: 100%;
            width: 3rem;
        }
    }
</style>
