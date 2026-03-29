import { register, getLocaleFromNavigator, init } from "svelte-i18n";

register("en-US", () => import("../translations/en.json"));
register("vi", () => import("../translations/vi.json"));
register("jp", () => import("../translations/jp.json"));

init({
    fallbackLocale: "en-US",
    initialLocale: getLocaleFromNavigator(),
});
