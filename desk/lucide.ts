import * as LucideIcons from "lucide-static";

const icons: Record<string, string> = {};

function processIcons(source: any) {
  if (!source || typeof source !== "object") return;
  for (const icon in source) {
    if (icon === "default" || icon === "__esModule") {
      continue;
    }
    let iconSvg = source[icon];
    if (!iconSvg || typeof iconSvg !== "string") {
      continue;
    }

    // set stroke-width to 1.5
    if (iconSvg.includes("stroke-width")) {
      iconSvg = iconSvg.replace(/stroke-width="2"/g, 'stroke-width="1.5"');
    }
    icons[icon] = iconSvg;

    const dashKeys = camelToDash(icon);
    for (const dashKey of dashKeys) {
      if (dashKey !== icon) {
        icons[dashKey] = iconSvg;
      }
    }
  }
}

processIcons(LucideIcons);
if ((LucideIcons as any).default && typeof (LucideIcons as any).default === "object") {
  processIcons((LucideIcons as any).default);
}

export default icons;

function camelToDash(key: string) {
  // barChart2 -> bar-chart-2
  // (PascalCase keys from newer lucide-static, e.g. TriangleAlert, must not get a leading dash)
  const withNumber = key
    .replace(/[A-Z0-9]/g, (m) => "-" + m.toLowerCase())
    .replace(/^-/, "");
  // barChart2 -> bar-chart2
  const withoutNumber = key
    .replace(/[A-Z]/g, (m) => "-" + m.toLowerCase())
    .replace(/^-/, "");

  if (withNumber !== withoutNumber) {
    // both are required because unplugin icon resolver doesn't put a dash before numbers
    return [withNumber, withoutNumber];
  }
  return [withNumber];
}
