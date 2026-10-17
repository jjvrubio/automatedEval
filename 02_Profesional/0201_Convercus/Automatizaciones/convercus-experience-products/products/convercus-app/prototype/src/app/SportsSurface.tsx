import { useState, type ReactNode } from "react";
import { createPortal } from "react-dom";
import { Link } from "react-router-dom";
import type { BrandArtifact } from "@/demo-factory/contracts";

// One React tree and provider; the iframe supplies only a mobile viewport, never a second bootstrap.
export function SportsSurface({ surface, demoId, brand, children }: {
  surface: "web" | "app";
  demoId: string;
  brand: BrandArtifact;
  children: ReactNode;
}) {
  const [host, setHost] = useState<HTMLElement>();
  const query = `?demo=${encodeURIComponent(demoId)}`;
  if (surface === "web") return <>
    <nav className="sports-surface-toolbar" aria-label="Superficie de la demo"><span>Vista Web · mismo recorrido al cambiar de vista</span><Link to={`/showcase${query}`}>Ver como App</Link></nav>
    {children}
  </>;
  return <main className="showcase-page showcase-page--sports">
    <header className="showcase-toolbar"><div><p className="eyebrow">Vista App · recorrido compartido con Web</p><h1>{brand.name} en iPhone</h1></div><Link className="showcase-close" to={`/${query}`}>Ver como Web</Link></header>
    <section className="iphone-stage" aria-label={`Simulación visual de ${brand.name} en un iPhone`}>
      <div className="iphone-device iphone-device--sports">
        <span className="iphone-device__speaker" aria-hidden="true" />
        <span className="iphone-device__button iphone-device__button--action" aria-hidden="true" />
        <span className="iphone-device__button iphone-device__button--volume-up" aria-hidden="true" />
        <span className="iphone-device__button iphone-device__button--volume-down" aria-hidden="true" />
        <span className="iphone-device__button iphone-device__button--power" aria-hidden="true" />
        <iframe className="iphone-device__screen" title={`${brand.name} — vista App`}
          srcDoc={'<!doctype html><html lang="es"><head><meta name="viewport" content="width=device-width,initial-scale=1" /></head><body><div id="sports-app-root"></div></body></html>'}
          onLoad={event => {
            const doc = event.currentTarget.contentDocument;
            if (!doc) return;
            doc.title = `${brand.name} — vista App`;
            const base = doc.createElement("base"); base.href = document.baseURI; doc.head.append(base);
            document.querySelectorAll('style, link[rel="stylesheet"]').forEach(node => doc.head.append(node.cloneNode(true)));
            Object.entries(brand.cssVariables).forEach(([key, value]) => doc.documentElement.style.setProperty(key, value));
            setHost(doc.getElementById("sports-app-root") ?? undefined);
          }} />
        {host && createPortal(children, host)}
        <span className="iphone-device__home-indicator" aria-hidden="true" />
      </div>
    </section>
    <p className="showcase-note">Desplázate dentro del teléfono. «Ver como Web» conserva este recorrido en la misma pestaña.</p>
  </main>;
}
