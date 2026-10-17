import { SportsCommerceHistory, SportsLoyaltyPanel } from "./SportsRelationshipPanels";
import type { SportsDemoAction, SportsUserSnapshot } from "@/demo-factory/sports-season/contracts";

export interface SportsDrafts {
  visitorName: string;
  interests: string[];
  frequency: string;
  goal: string;
}

interface PanelProps {
  user: SportsUserSnapshot;
  busy: boolean;
  run: (action: SportsDemoAction) => Promise<boolean>;
  drafts: SportsDrafts;
  update: (patch: Partial<SportsDrafts>) => void;
}

const money = (cents: number) => new Intl.NumberFormat("es-ES", { style: "currency", currency: "EUR" }).format(cents / 100);

export function SportsPersonPanel({ user, busy, run, drafts, update, choosePerson, qrEventRef, registered }: PanelProps & {
  choosePerson: (personRef: string) => void;
  qrEventRef: string;
  registered: boolean;
}) {
  const person = user.person;
  return <section className="sports-user-section" aria-labelledby="person-selection-title">
    <div className="sports-section-title"><div><p className="sports-kicker">01 · Una persona, distintas relaciones</p><h2 id="person-selection-title">¿Con quién quieres probar la demo?</h2></div></div>
    <p className="sports-note">Personas y compras ficticias. Cada persona conserva su recorrido durante esta sesión; no es un inicio de sesión.</p>
    <div className="sports-people">
      {user.configuration.people.map((item) => <article className={`sports-person-card${person?.id === item.id ? " is-selected" : ""}`} key={item.id}>
        <p className="sports-kicker">{item.id}</p><h3>{item.name}</h3>
        <p>{item.customerRelationship === "established" ? "Cliente conocido" : "No cliente"}<br />{item.membershipStatus === "member" ? `Miembro de ${user.relationship?.program.name ?? "Brisa Club"}` : "No miembro del programa"}</p>
        {item.id === user.configuration.primaryPersonRef && <p className="sports-tag">Caso principal</p>}
        <button type="button" className="sports-button sports-button--outline" aria-pressed={person?.id === item.id} disabled={busy} onClick={() => choosePerson(item.id)}>{`Elegir a ${item.name}`}</button>
      </article>)}
    </div>
    <div className="sports-qr-entry">
      <div><h3>¿Vienes desde el QR del evento?</h3><p>Simula la entrada a la inscripción de Carrera. El registro de presencia llegará después.</p></div>
      <button type="button" className="sports-button" disabled={busy || registered || user.intention === "information"} onClick={() => void run({ type: "sports-registration-qr", eventRef: qrEventRef })}>Leer QR de inscripción</button>
    </div>
    {user.registrationEntry && <div className="sports-panel sports-entry-status" role="status">
      <h3>QR de inscripción · simulado</h3>
      <p>{!person ? "Elige arriba qué persona reconoce esta simulación." : user.registrationEntry.recognized ? "Cliente reconocido. Recuperamos sus datos ficticios y su estado de programa; no hace falta volver a introducirlos." : "Persona no reconocida. Puedes participar sin ser cliente: elige Participar y completa el nombre ficticio para la inscripción."}</p>
      <p className="sports-note">Esta entrada no acredita presencia ni confirma la inscripción.</p>
    </div>}
    {person && <section className="sports-panel sports-person-summary" aria-labelledby="selected-person-title">
      <p className="sports-kicker">Persona seleccionada · datos ficticios conocidos</p>
      <h2 id="selected-person-title">{person.name}</h2>
      <dl className="sports-facts">
        <div><dt>Relación con la marca</dt><dd>{person.customerRelationship === "established" ? "Cliente conocido" : "No cliente · sin relación comercial establecida"}</dd></div>
        <div><dt>Programa de fidelización</dt><dd>{person.membershipStatus === "member" ? `Miembro de ${user.relationship?.program.name ?? "Brisa Club"}` : "No pertenece al programa"}</dd></div>
        {person.knownData && <><div><dt>Localidad conocida</dt><dd>{person.knownData.city}</dd></div><div><dt>Práctica conocida en el escenario</dt><dd>{person.knownData.usualSport}</dd></div></>}
      </dl>
      {user.relationship ? <><SportsCommerceHistory relationship={user.relationship} /><SportsLoyaltyPanel relationship={user.relationship} /></> : person.customerRelationship === "established" ? <>
        <h3>Compras ficticias registradas</h3>
        <ul className="sports-purchases">{person.purchases.map((purchase) => <li key={purchase.id}><div><strong>{purchase.description}</strong><time dateTime={purchase.date}>{new Date(purchase.date).toLocaleDateString("es-ES", { timeZone: "UTC" })}</time></div><span>{money(purchase.amountCents)}</span></li>)}</ul>
      </> : <p>No hay historial transaccional ni datos de cliente. Un evento puede ser el comienzo de la relación; inscribirte no crea una cuenta ni te incorpora al programa.</p>}
      {user.counterfactual && <aside className="sports-counterfactual" aria-label="Contrafactual de fidelización">
        <p className="sports-kicker">Contrafactual · no es saldo disponible</p>
        <h3>{user.counterfactual.potentialPoints} puntos potenciales</h3>
        <p>Con tus compras realizadas ({money(user.counterfactual.totalCents)}), si hubieras pertenecido al programa, habrías obtenido estos puntos.</p>
        <p className="sports-note">Ejemplo ficticio: {user.configuration.counterfactualPointsPerEuro} punto por euro completo. No se abonan puntos ni se crean beneficios retroactivos.</p>
      </aside>}
      {person.program && <aside className="sports-program" aria-label="Estado ficticio del programa">
        <p className="sports-kicker">Estado del programa · simulado</p>
        <h3>{person.program.points} puntos · nivel {person.program.level}</h3>
        <p>Saldo ficticio de este miembro, separado del contrafactual de quien no pertenece al programa.</p>
        <ul>{person.program.benefits.map((benefit) => <li key={benefit}>{benefit}</li>)}</ul>
      </aside>}
    </section>}
    {person && <section className="sports-intention" aria-labelledby="intention-title">
      <p className="sports-kicker">02 · Tu decisión en este encuentro</p><h2 id="intention-title">¿Qué quieres hacer ahora?</h2>
      <div className="sports-intention-actions">
        <button className="sports-button" type="button" aria-pressed={user.intention === "participate"} disabled={busy || user.intention === "information"} onClick={() => void run({ type: "sports-intention", personRef: person.id, intention: "participate" })}>Participar</button>
        <button className="sports-button sports-button--outline" type="button" aria-pressed={user.intention === "information"} disabled={busy || user.intention === "participate"} onClick={() => void run({ type: "sports-intention", personRef: person.id, intention: "information" })}>No participar, pero quiero recibir información</button>
      </div>
      <p className="sports-note">No participar no significa falta de interés. Para probar otra intención, reinicia el recorrido.</p>
    </section>}
    {person?.customerRelationship === "not-established" && user.intention === "participate" && <section className="sports-panel sports-visitor" aria-labelledby="visitor-title">
      <h3 id="visitor-title">Datos mínimos para la inscripción</h3>
      {user.visitorIdentified ? <p>Nombre para esta inscripción: <strong>{person.name}</strong>. Sigues sin ser cliente ni miembro del programa.</p> : <form noValidate onSubmit={e => { e.preventDefault(); void run({ type: "sports-identify-visitor", personRef: person.id, name: drafts.visitorName }); }}>
        <label className="sports-field">Nombre ficticio para esta demo<input type="text" value={drafts.visitorName} maxLength={80} onChange={e => update({ visitorName: e.target.value })} disabled={busy} /></label>
        <button className="sports-button" disabled={busy}>Continuar con este nombre</button>
      </form>}
      <p className="sports-note">La identificación completa y el alta de cliente se narran; no se ejecutan. Puedes completar aquí la participación deportiva simulada.</p>
    </section>}
  </section>;
}

export function SportsInterestPanel({ user, busy, run, drafts, update }: PanelProps) {
  if (!user.person || user.intention !== "information") return null;
  const personRef = user.person.id;
  return <section className="sports-panel sports-interest-panel" aria-labelledby="interests-title">
    <p className="sports-kicker">Recibir información · sin participar</p><h2 id="interests-title">¿Qué te interesa?</h2>
    <form noValidate onSubmit={e => { e.preventDefault(); void run({ type: "sports-interests", personRef, values: drafts.interests }); }}>
      <fieldset disabled={busy}><legend>Elige los temas sobre los que querrías saber más</legend><div className="sports-interest-options">{user.configuration.interests.map(item => <label key={item.value}>
        <input type="checkbox" checked={drafts.interests.includes(item.value)} onChange={e => update({ interests: e.target.checked ? [...drafts.interests, item.value] : drafts.interests.filter(value => value !== item.value) })} />{item.label}
      </label>)}</div></fieldset>
      <button className="sports-button" disabled={busy}>Registrar intereses</button>
    </form>
    {user.declaredInterests && <div className="sports-interest-confirmation" role="status"><h3>Interés declarado registrado</h3><p>{user.declaredInterests.values.map(value => user.configuration.interests.find(item => item.value === value)?.label).join(" · ")}</p><p>Sin inscripción, presencia, esfuerzo ni insignia. No se envían comunicaciones ni se crea una suscripción real.</p></div>}
  </section>;
}

export function SportsVoluntaryPanel({ user, busy, run, drafts, update }: PanelProps) {
  if (!user.person) return null;
  const personRef = user.person.id;
  return <section className="sports-panel sports-voluntary" aria-labelledby="voluntary-title">
    <p className="sports-kicker">Después de inscribirte · tú decides</p><h3 id="voluntary-title">Información adicional voluntaria</h3>
    {!user.voluntary ? <>
      <p>Si compartes al menos una respuesta, podrás consultar la «{user.configuration.incentive.title}» aquí mismo. También puedes continuar sin responder.</p>
      <form noValidate onSubmit={e => { e.preventDefault(); void run({ type: "sports-voluntary", personRef, decision: "provided", frequency: drafts.frequency, goal: drafts.goal }); }}>
        <div className="sports-voluntary-fields">
          <label className="sports-field">Frecuencia de práctica (opcional)<select value={drafts.frequency} disabled={busy} onChange={e => update({ frequency: e.target.value })}><option value="">Sin respuesta</option>{user.configuration.frequencies.map(item => <option key={item.value} value={item.value}>{item.label}</option>)}</select></label>
          <label className="sports-field">Objetivo (opcional)<select value={drafts.goal} disabled={busy} onChange={e => update({ goal: e.target.value })}><option value="">Sin respuesta</option>{user.configuration.goals.map(item => <option key={item.value} value={item.value}>{item.label}</option>)}</select></label>
        </div>
        <p className="sports-note">Son respuestas declaradas por ti, no observaciones de la marca. La guía es un incentivo por información, separado de la insignia deportiva y de la pertenencia al club.</p>
        <div className="sports-intention-actions"><button className="sports-button" disabled={busy}>Compartir información y obtener la guía</button><button className="sports-button sports-button--outline" type="button" disabled={busy} onClick={() => void run({ type: "sports-voluntary", personRef, decision: "skipped" })}>Continuar sin aportar información</button></div>
      </form>
    </> : user.voluntary.decision === "skipped" ? <p>Has continuado sin aportar información adicional. Tu inscripción y tu posibilidad de obtener la insignia se mantienen.</p> : <>
      <p>Información declarada: {[user.configuration.frequencies.find(item => item.value === user.voluntary?.frequency)?.label, user.configuration.goals.find(item => item.value === user.voluntary?.goal)?.label].filter(Boolean).join(" · ")}.</p>
      {user.incentive && <div className="sports-incentive" role="status"><p className="sports-kicker">Incentivo por información disponible</p><h3>{user.incentive.title}</h3><details><summary>Abrir guía</summary><ul>{user.incentive.content.map(item => <li key={item}>{item}</li>)}</ul></details><p className="sports-note">Este contenido no es una insignia, puntos ni un alta en el programa.</p></div>}
    </>}
  </section>;
}

export function SportsEquipmentPanel({ user }: { user: SportsUserSnapshot }) {
  if (!user.recommendations.length) return null;
  return <section className="sports-equipment" aria-labelledby="equipment-title"><p className="sports-kicker">Para el evento que has elegido</p><h2 id="equipment-title">Equipamiento para Carrera</h2><p className="sports-note">Sugerencias editoriales de esta demo, comunes para quienes eligen Carrera. Sin selección automática, precios ni compra.</p><div className="sports-equipment-grid">{user.recommendations.map(item => <article key={item.title}><h3>{item.title}</h3><p>{item.description}</p></article>)}</div></section>;
}
