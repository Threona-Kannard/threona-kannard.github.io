import type { PlaylistData, Track } from "$lib/types/spotify.dto";
import type { PageLoad, EntryGenerator } from "./$types";
import { error } from "@sveltejs/kit";

export const entries: EntryGenerator = () => {
    return [
        { name: "childhood" },
        { name: "coast-to-coast" },
        { name: "hero-journey" },
        { name: "moonlight" },
        { name: "radio-gac-xep" },
    ];
};

export const load: PageLoad = async ({ params }) => {
    const playlistData = (await import(
        `$lib/data/json/${params.name}-playlist-info.json`
    ).catch(() => {
        error(404, "Playlist not found.");
    })) as unknown as PlaylistData;
    const playlistTracks = (await import(
        `$lib/data/json/${params.name}-playlist.json`
    ).catch(() => {
        error(404, "Playlist not found.");
    })) as unknown as { tracks: Track[] };

    return {
        playlistData,
        tracks: playlistTracks.tracks,
    };
};
