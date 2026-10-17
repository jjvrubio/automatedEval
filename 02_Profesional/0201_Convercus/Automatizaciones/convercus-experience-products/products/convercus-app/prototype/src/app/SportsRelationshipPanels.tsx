import type { PersonRelationship } from "@/demo-factory/sports-season/relationship-contract";
import type { SportsSnapshot } from "@/demo-factory/sports-season/contracts";
import { Icon } from "@/ui/Icon";

const money = (cents: number) => new Intl.NumberFormat("es-ES", { style: "currency", currency: "EUR" }).format(cents / 100);
const date = (value: string) => new Intl.DateTimeFormat("es-ES", { day: "numeric", month: "short", year: "numeric", timeZone: "Europe/Madrid" }).format(new Date(value));
const channels: Record<string,string> = { store: "Tienda", web: "Web", app: "App" };
const categories: Record<string,string> = { running: "Running", running_apparel: "Textil running", hydration: "Hidratación", fitness: "Fitness", accessories: "Accesorios", nutrition: "Nutrición", wearables: "Dispositivos deportivos", sailing: "Vela", sailing_apparel: "Textil náutico", beach_volleyball: "Vóley playa" };
const experienceStates = { available: "Disponible", enrolled: "Inscrito", active: "En curso", completed: "Completado" };

export function SportsCommerceHistory({ relationship }: { relationship: PersonRelationship }) {
  const { transactions, totalCents } = relationship;
  return <section className="sports-commerce" aria-label="Historial comercial">
    <div className="sports-section-title"><div><p className="sports-kicker">Tu relación con Brisa Sport</p><h3>Historial comercial</h3></div></div>
    <p className="sports-commerce-total"><strong>{money(totalCents)}</strong><span>{transactions.length} compras registradas · gasto acumulado</span></p>
    {transactions.length ? <details className="sports-transactions" open>
      <summary>Ver las {transactions.length} transacciones</summary>
      <ul className="sports-purchases">{transactions.map(t => <li key={t.id}>
        <div><strong>{t.product}</strong><time dateTime={t.occurredAt}>{date(t.occurredAt)}</time>
          <span className="sports-transaction-meta">{channels[t.channel] ?? t.channel} · {categories[t.category] ?? t.category} · {t.quantity} ud.</span>
        </div><span>{money(t.grossCents)}</span>
      </li>)}</ul>
    </details> : <p>Sin compras previas. Puedes acceder al evento sin ser cliente ni miembro.</p>}
    <p className="sports-note">Compras ficticias observadas. Este historial comercial no es un movimiento de puntos.</p>
  </section>;
}

export function SportsLoyaltyPanel({ relationship }: { relationship: PersonRelationship }) {
  const { loyalty, counterfactual, program } = relationship;
  return <>
    {loyalty.membershipStatus === "active" ? <aside className="sports-program" aria-label="Estado del programa">
      <p className="sports-kicker">{program.name} · Membresía activa</p>
      <h3>{loyalty.pointsBalance} puntos · nivel {loyalty.actualLevel?.name}</h3>
      <p>Saldo actual en esta demo · miembro {loyalty.membershipId}</p>
      {loyalty.joinedAt && <p className="sports-note">Miembro desde {date(loyalty.joinedAt)}</p>}
      <ul>{program.levels.find(l => l.id === loyalty.actualLevel?.id)?.benefits.map(b => <li key={b}>{b}</li>)}</ul>
    </aside> : <div className="sports-membership-empty"><strong>No miembro de {program.name}</strong><p>Sin saldo de puntos ni nivel asignado.</p></div>}
    {counterfactual && <aside className="sports-counterfactual" aria-label="Contrafactual de fidelización">
      <p className="sports-kicker">Simulación / contrafactual · no es saldo disponible</p>
      <h3>{counterfactual.hypotheticalPoints} puntos potenciales</h3>
      <p>Con tus compras registradas ({money(counterfactual.basisCents)}), si hubieras pertenecido a {program.name}, habrías alcanzado el nivel <strong>{counterfactual.hypotheticalLevel.name}</strong>.</p>
      <ul>{counterfactual.hypotheticalBenefits.map(b => <li key={b}>{b}</li>)}</ul>
      <p><strong>{counterfactual.disclaimer}</strong></p>
      <p className="sports-note">Regla exclusiva de esta demo: {program.pointsPerFullEuro} punto por euro completo de gasto elegible acumulado. No son derechos adquiridos ni reglas generales de Convercus.</p>
    </aside>}
  </>;
}

export function SportsSelfService({ snapshot, onEvent }: { snapshot: SportsSnapshot; onEvent: () => void }) {
  const user = snapshot.userPlane;
  const person = user?.person, relationship = user?.relationship;
  if (!person || !relationship) return null;
  const { loyalty, badges, coupons, news, experiences, program } = relationship;
  return <main id="sports-main" className="sports-main sports-self-service">
    <header className="sports-self-hero">
      <div><p className="sports-kicker">Self Service · {program.name}</p><h1>Tu relación continúa.</h1><p>Hola, {person.name}. Tus compras, tu club y tus experiencias, en un mismo lugar.</p></div>
      <button type="button" className="sports-button sports-button--outline" onClick={onEvent}>Volver a la temporada</button>
    </header>
    <section className="sports-self-profile sports-panel" aria-labelledby="self-profile">
      <span className="sports-avatar" aria-hidden="true"><Icon name="user" /></span>
      <div><p className="sports-kicker">Perfil · {person.id}</p><h2 id="self-profile">{person.name}</h2>
        <p>{person.customerRelationship === "established" ? "Cliente conocido" : "No cliente"} · {loyalty.membershipStatus === "active" ? "Miembro activo" : "No miembro"}</p>
        {person.knownData && <p className="sports-note">{person.knownData.city} · {person.knownData.usualSport}</p>}
      </div>
    </section>
    <div className="sports-self-grid">
      <section className="sports-panel sports-self-loyalty" aria-label="Fidelización">
        <h2>Puntos y nivel</h2><SportsLoyaltyPanel relationship={relationship} />
        {loyalty.membershipStatus === "non_member" && <details className="sports-join">
          <summary>Conocer {program.name}</summary><p>Una oportunidad de incorporarte al programa y mantener la relación más allá del evento.</p>
          <p>El alta está narrada en esta demo. Consultar esta información o participar no te convierte en miembro ni te concede puntos retroactivos.</p>
        </details>}
      </section>
      <section className="sports-panel" aria-labelledby="self-badges"><p className="sports-kicker">Reconocimientos que te acompañan</p><h2 id="self-badges">Insignias</h2>
        {badges.length ? <ul className="sports-badge-list">{badges.map(b => <li key={b.id}>
          <Icon name="star" size={28} /><div><h3>{b.title}</h3><p>{b.origin === "sports_season" ? "Sports Season · obtenida en esta sesión" : "Programa de fidelización"}</p>
            <time dateTime={b.awardedAt}>{date(b.awardedAt)}</time>
            {b.origin === "sports_season" && <p className="sports-note">Inscripción aceptada + presencia simulada + esfuerzo autodeclarado.</p>}
          </div>
        </li>)}</ul> : <p>Aún no tienes insignias. Completa Carrera para obtener tu primer reconocimiento deportivo.</p>}
        <p className="sports-note">Una insignia reconoce tu participación. No modifica tu saldo, nivel ni cupones.</p>
      </section>
      <section className="sports-panel" aria-labelledby="self-coupons"><p className="sports-kicker">Ventajas del programa</p><h2 id="self-coupons">Cupones</h2>
        {coupons.length ? <ul className="sports-content-list">{coupons.map(c => <li key={c.id}><h3>{c.title}</h3><span className="sports-tag">{c.status === "available" ? "Disponible" : c.status}</span><p>Del {date(c.validFrom)} al {date(c.validUntil)}</p><p className="sports-note">Beneficio simulado · sin canje en esta demo.</p></li>)}</ul> : <p>No tienes cupones asignados.</p>}
      </section>
      <section className="sports-panel" aria-labelledby="self-experiences"><p className="sports-kicker">Próximos encuentros y participación</p><h2 id="self-experiences">Experiences</h2>
        {experiences.length ? <ul className="sports-content-list">{experiences.map(e => <li key={e.id}><span className="sports-tag">{experienceStates[e.state]}</span><h3>{e.name}</h3><p>{e.eligibility === "OPEN" ? "Abierta · sin membresía necesaria" : `Acceso por nivel ${program.levels.find(l => l.id === e.eligibility)?.name ?? e.eligibility}`}</p>
          {e.eventRef && <button type="button" className="sports-button sports-button--outline" onClick={onEvent}>Ver mi participación</button>}
        </li>)}</ul> : <><p>Puedes comenzar por la Carrera abierta de Sports Season.</p><button type="button" className="sports-button" onClick={onEvent}>Explorar el evento</button></>}
      </section>
    </div>
    <section className="sports-panel sports-self-history"><SportsCommerceHistory relationship={relationship} /></section>
    <section className="sports-self-news" aria-labelledby="self-news"><p className="sports-kicker">Actualidad de la comunidad</p><h2 id="self-news">Noticias</h2>
      <div className="sports-news-grid">{news.map(n => <article className="sports-panel" key={n.id}><time dateTime={n.publishedAt}>{date(n.publishedAt)}</time><h3>{n.title}</h3><p>{n.summary}</p></article>)}</div>
    </section>
    {(user.declaredInterests || user.voluntary?.decision === "provided") && <section className="sports-panel sports-self-declarations"><h2>Lo que has compartido</h2>
      {user.declaredInterests && <p>Intereses: {user.declaredInterests.values.map(v => user.configuration.interests.find(i => i.value === v)?.label).join(" · ")}</p>}
      {user.voluntary?.decision === "provided" && <p>{[user.configuration.frequencies.find(f => f.value === user.voluntary?.frequency)?.label, user.configuration.goals.find(g => g.value === user.voluntary?.goal)?.label].filter(Boolean).join(" · ")}</p>}
      <p className="sports-note">Información declarada por ti. No implica participación ni intención de compra.</p>
    </section>}
  </main>;
}
