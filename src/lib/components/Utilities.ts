export function randomInt(min: number, max: number): number {
    return Math.floor(Math.random() * (max - min + 1)) + min;
}

export function randomFromArray<T>(items: T[]): T {
    if (!items.length) {
        throw new Error("randomFromArray requires at least one item");
    }

    return items[randomInt(0, items.length - 1)];
}

export function randomFloat(min: number, max: number): number {
    return Math.random() * (max - min) + min;
}

export function clamp(value: number, min: number, max: number): number {
    return Math.min(Math.max(value, min), max);
}
