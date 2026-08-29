import type { PlaylistData } from "$lib/types/spotify.dto";
import { error } from "@sveltejs/kit";

const ERROR_MSG = "That playlist is not playing now...";

export async function load() {
    const childhoodPlaylist = (await import(
        `$lib/data/json/childhood-playlist-info.json`
    ).catch(() => {
        error(404, ERROR_MSG);
    })) as unknown as PlaylistData;
    const ctcPlaylist = (await import(
        `$lib/data/json/coast-to-coast-playlist-info.json`
    ).catch(() => {
        error(404, ERROR_MSG);
    })) as unknown as PlaylistData;
    const hjPlaylist = (await import(
        `$lib/data/json/hero-journey-playlist-info.json`
    ).catch(() => {
        error(404, ERROR_MSG);
    })) as unknown as PlaylistData;
    const mlPlaylist = (await import(
        `$lib/data/json/moonlight-playlist-info.json`
    ).catch(() => {
        error(404, ERROR_MSG);
    })) as unknown as PlaylistData;
    const rgxPlaylist = (await import(
        `$lib/data/json/radio-gac-xep-playlist-info.json`
    ).catch(() => {
        error(404, ERROR_MSG);
    })) as unknown as PlaylistData;

    return {
        playlists: {
            childhoodPlaylist,
            ctcPlaylist,
            hjPlaylist,
            mlPlaylist,
            rgxPlaylist
        },
    };
}
