import fs from 'node:fs';
import path from 'node:path';

const args = {};
for (let i = 2; i < process.argv.length; i += 1) {
  const arg = process.argv[i];

  if (!arg.startsWith('--')) {
    continue;
  }

  const equalsIndex = arg.indexOf('=');
  const key = equalsIndex >= 0 ? arg.slice(2, equalsIndex) : arg.slice(2);

  if (equalsIndex >= 0) {
    args[key] = arg.slice(equalsIndex + 1);
    continue;
  }

  const nextValue = process.argv[i + 1];
  if (nextValue && !nextValue.startsWith('--')) {
    args[key] = nextValue;
    i += 1;
  } else {
    args[key] = true;
  }
}

const repoRoot = process.cwd();
const filePath = args.file ? path.resolve(repoRoot, args.file) : null;
const folderPath = args.folder ? path.resolve(repoRoot, args.folder) : null;
const title = args.title || 'New gallery';
const date = args.date || '01 2025';
const variant = args.variant || 'featured';

if (!filePath || !folderPath) {
  console.error('Usage: node scripts/add-gallery-entry.mjs --file src/translations/en.json --folder src/lib/assets/images/galleries/buildnbrew25 --title "Saigon Build&Brew" --date "05 2025" --variant featured');
  process.exit(1);
}

if (!fs.existsSync(folderPath)) {
  console.error(`Folder not found: ${folderPath}`);
  process.exit(1);
}

const supportedExtensions = new Set(['.jpg', '.jpeg', '.png', '.webp', '.gif', '.mp4', '.webm', '.mov', '.avi', '.ogg']);

const collectFiles = (dir) => {
  const entries = fs.readdirSync(dir, { withFileTypes: true });
  const files = [];

  for (const entry of entries) {
    const fullPath = path.join(dir, entry.name);
    if (entry.isDirectory()) {
      files.push(...collectFiles(fullPath));
    } else if (supportedExtensions.has(path.extname(entry.name).toLowerCase())) {
      files.push(fullPath);
    }
  }

  return files;
};

const getSortValue = (fileName) => {
  const match = fileName.match(/(\d+)/g);
  if (!match) return Number.MAX_SAFE_INTEGER;
  return Number(match[match.length - 1]);
};

const files = collectFiles(folderPath).sort((a, b) => {
  const aName = path.basename(a).toLowerCase();
  const bName = path.basename(b).toLowerCase();
  const aValue = getSortValue(aName);
  const bValue = getSortValue(bName);

  if (aValue !== bValue) {
    return aValue - bValue;
  }

  return aName.localeCompare(bName);
});

const images = files.map((file) => {
  const relative = path.relative(repoRoot, file).split(path.sep).join('/');
  return `/${relative}`;
});

const locale = JSON.parse(fs.readFileSync(filePath, 'utf8'));
if (!locale.page) locale.page = {};
if (!locale.page.galleries) locale.page.galleries = { title: 'My galleries', items: [] };
if (!Array.isArray(locale.page.galleries.items)) locale.page.galleries.items = [];

const item = { title, date, images, variant };
const existingIndex = locale.page.galleries.items.findIndex((entry) => entry.title === title);

if (existingIndex >= 0) {
  locale.page.galleries.items[existingIndex] = item;
} else {
  locale.page.galleries.items.push(item);
}

fs.writeFileSync(filePath, `${JSON.stringify(locale, null, 4)}\n`);
console.log(`Updated ${path.relative(repoRoot, filePath)} with ${images.length} media entries.`);
