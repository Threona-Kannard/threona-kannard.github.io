import { register, getLocaleFromNavigator, init } from "svelte-i18n";

register("en-US", () => import("../translations/en.json"));
register("vi", () => import("../translations/vi.json"));
register("jp", () => import("../translations/jp.json"));

const navigatorLocale = getLocaleFromNavigator();
const initialLocale = navigatorLocale && ["en-US", "vi", "jp"].includes(navigatorLocale)
    ? navigatorLocale
    : "en-US";

init({
    fallbackLocale: "en-US",
    initialLocale,
});
