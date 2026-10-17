import { useEffect, useState } from "react";
import { Link, NavLink, Route, Routes, useLocation } from "react-router-dom";
import type {
  ActivityItem,
  AppSnapshot,
  CouponReadModel as Coupon,
  ResolvedDemoRuntime,
} from "@/demo-factory/contracts";
import { FeedbackState } from "@/ui/FeedbackState";
import { Icon, type IconName } from "@/ui/Icon";

function formatPoints(points: number): string {
  return new Intl.NumberFormat("es-ES").format(points);
}

function SectionHeading({
  eyebrow,
  title,
  linkTo,
}: {
  eyebrow?: string;
  title: string;
  linkTo?: string;
}) {
  return (
    <div className="section-heading">
      <div>
        {eyebrow && <p className="eyebrow">{eyebrow}</p>}
        <h2>{title}</h2>
      </div>
      {linkTo && (
        <Link className="text-link" to={linkTo}>
          Ver todo <Icon name="arrow" size={16} />
        </Link>
      )}
    </div>
  );
}

function CouponCard({ coupon, featured = false }: { coupon: Coupon; featured?: boolean }) {
  return (
    <article className={`coupon-card coupon-card--${coupon.tone}${featured ? " coupon-card--featured" : ""}`}>
      <div className="coupon-card__topline">
        <span className="coupon-card__icon" aria-hidden="true">
          <Icon name={coupon.icon} size={22} />
        </span>
        <span className="coupon-card__tag">{coupon.tag}</span>
      </div>
      <div>
        <h3>{coupon.title}</h3>
        <p>{coupon.description}</p>
      </div>
      <div className="coupon-card__footer">
        <span>{coupon.validUntil}</span>
        <span aria-hidden="true"><Icon name="arrow" size={18} /></span>
      </div>
    </article>
  );
}

function ActivityList({ items, compact = false }: { items: ActivityItem[]; compact?: boolean }) {
  if (items.length === 0) {
    return (
      <FeedbackState
        icon="activity"
        title="Aún no hay actividad"
        description="Tus movimientos y novedades aparecerán aquí."
      />
    );
  }

  return (
    <div className={`activity-list${compact ? " activity-list--compact" : ""}`}>
      {items.map((item) => (
        <article className="activity-item" key={item.id}>
          <span className={`activity-item__icon activity-item__icon--${item.tone}`} aria-hidden="true">
            <Icon name={item.icon} size={20} />
          </span>
          <div className="activity-item__content">
            <div className="activity-item__heading">
              <h3>{item.title}</h3>
              {item.points !== undefined && (
                <strong className={item.points >= 0 ? "points-positive" : ""}>
                  {item.points >= 0 ? "+" : ""}{item.points} pts
                </strong>
              )}
            </div>
            <p>{item.description}</p>
            <time dateTime={item.occurredAt}>{item.displayDate}</time>
          </div>
        </article>
      ))}
    </div>
  );
}

function HomePage({
  snapshot,
  guestAction,
  guestActionLabel,
  brandName,
  introductoryFraming,
}: {
  snapshot: AppSnapshot;
  guestAction: () => void;
  guestActionLabel?: string;
  brandName: ResolvedDemoRuntime["brand"]["name"];
  introductoryFraming?: string;
}) {
  const { member, coupons, activity, news } = snapshot;

  if (snapshot.guestPerspective) {
    const adventure = snapshot.guestPerspective;
    return (
      <main id="main-content" className="adventure-page">
        <header className="adventure-heading">
          <p className="eyebrow">Mi aventura · {brandName}</p>
          <h1 id="adventure-title">{adventure.huntName}</h1>
          {introductoryFraming && <p>{introductoryFraming}</p>}
        </header>
        <section className="adventure-next" aria-labelledby="next-action-title">
          <p className="eyebrow" id="next-action-title">{guestActionLabel ? "Tu siguiente paso" : "Resultado de la aventura"}</p>
          <p className="adventure-message" role="status">{adventure.message}</p>
          {guestActionLabel && <button className="secondary-action" type="button" onClick={guestAction}>{guestActionLabel}<Icon name="arrow" size={18} /></button>}
          <p className="adventure-count">{adventure.discoveredClueCount} {adventure.discoveredClueCount === 1 ? "pista descubierta" : "pistas descubiertas"}</p>
        </section>
        <section aria-labelledby="guests-title">
          <h2 id="guests-title">Quién puede explorar</h2>
          <div className="adventure-guests">
            {adventure.subjects.map((subject) => (
              <article className="adventure-guest" key={subject.id}>
                <h3>{subject.label}</h3>
                <p>{subject.status} · {subject.clueCount} {subject.clueCount === 1 ? "pista aportada" : "pistas aportadas"}</p>
              </article>
            ))}
          </div>
          <p className="adventure-session">{adventure.sessionLabel}</p>
        </section>
      </main>
    );
  }

  return (
    <main id="main-content" className="page-stack home-page">
      <section className="welcome-row" aria-labelledby="welcome-title">
        <div>
          <p className="eyebrow">Buenos días</p>
          <h1 id="welcome-title">Hola, {member.name}</h1>
        </div>
        <Link className="icon-button" to="/activity" aria-label="Ver notificaciones y actividad">
          <Icon name="bell" size={22} />
          <span className="notification-dot" aria-hidden="true" />
        </Link>
      </section>

      <section className="balance-card" aria-label="Resumen de fidelización">
        <div className="balance-card__glow" aria-hidden="true" />
        <div className="balance-card__heading">
          <div>
            <span className="balance-card__label">Tu saldo</span>
            <p className="balance-card__points">{formatPoints(member.points)} <small>pts</small></p>
          </div>
          <span className="level-badge"><Icon name="sparkles" size={15} /> {member.level}</span>
        </div>
        <div className="progress-block">
          <div className="progress-block__labels">
            <span>{member.progress}% hacia {member.nextLevel}</span>
            <span>{formatPoints(member.pointsToNextLevel)} pts restantes</span>
          </div>
          <div className="progress-track" role="progressbar" aria-valuenow={member.progress} aria-valuemin={0} aria-valuemax={100} aria-label={`Progreso hacia ${member.nextLevel}`}>
            <span style={{ width: `${member.progress}%` }} />
          </div>
        </div>
        <Link className="balance-card__action" to="/profile">
          Ver mi cuenta <Icon name="arrow" size={18} />
        </Link>
      </section>


      <section aria-labelledby="quick-title">
        <h2 className="sr-only" id="quick-title">Accesos rápidos</h2>
        <div className="quick-actions">
          <Link to="/benefits"><span><Icon name="ticket" size={23} /></span>Mis cupones</Link>
          <Link to="/activity"><span><Icon name="activity" size={23} /></span>Actividad</Link>
          <Link to="/profile"><span><Icon name="user" size={23} /></span>Mi perfil</Link>
          <Link reloadDocument={!snapshot.guestPerspective} to="/?demo=hospitality-family-adventure"><span><Icon name="compass" size={23} /></span>Búsqueda del tesoro</Link>
        </div>
      </section>

      <section aria-labelledby="benefits-title">
        <SectionHeading eyebrow="Para ti" title="Beneficios destacados" linkTo="/benefits" />
        <div className="coupon-grid" id="benefits-title">
          {coupons.slice(0, 2).map((coupon, index) => (
            <CouponCard coupon={coupon} featured={index === 0} key={coupon.id} />
          ))}
        </div>
      </section>

      <section className="story-card" aria-labelledby="story-title">
        <div className="story-card__art" aria-hidden="true">
          <span><Icon name="sparkles" size={34} /></span>
        </div>
        <div className="story-card__content">
          <p className="eyebrow">{news[0]?.category}</p>
          <h2 id="story-title">{news[0]?.title}</h2>
          <p>{news[0]?.summary}</p>
          <Link className="secondary-action" to="/benefits">Descubrir más</Link>
        </div>
      </section>

      <section aria-labelledby="activity-title">
        <SectionHeading title="Actividad reciente" linkTo="/activity" />
        <div id="activity-title"><ActivityList items={activity.slice(0, 2)} compact /></div>
      </section>
    </main>
  );
}

function BenefitsPage({ coupons }: { coupons: Coupon[] }) {
  return (
    <main id="main-content" className="page-stack">
      <header className="page-header">
        <p className="eyebrow">Tu selección</p>
        <h1>Beneficios</h1>
        <p>Ventajas disponibles para disfrutar ahora y propuestas seleccionadas para ti.</p>
      </header>
      <div className="filter-row" aria-label="Filtros de beneficios">
        <span className="filter-chip filter-chip--active">Todos</span>
        <span className="filter-chip">Disponibles</span>
        <span className="filter-chip">Próximamente</span>
      </div>
      <section aria-labelledby="coupon-list-title">
        <SectionHeading title={`${coupons.length} beneficios disponibles`} />
        <h2 className="sr-only" id="coupon-list-title">Listado de beneficios</h2>
        {coupons.length > 0 ? (
          <div className="coupon-grid coupon-grid--catalog">
            {coupons.map((coupon, index) => <CouponCard coupon={coupon} featured={index === 0} key={coupon.id} />)}
          </div>
        ) : (
          <FeedbackState icon="ticket" title="No hay beneficios disponibles" description="Vuelve pronto para descubrir nuevas ventajas." />
        )}
      </section>
    </main>
  );
}

function ActivityPage({ activity }: { activity: ActivityItem[] }) {
  return (
    <main id="main-content" className="page-stack">
      <header className="page-header">
        <p className="eyebrow">Todo al día</p>
        <h1>Actividad</h1>
        <p>Consulta tus puntos, beneficios y últimas interacciones.</p>
      </header>
      <section aria-labelledby="activity-list-title">
        <h2 className="section-title" id="activity-list-title">Últimos movimientos</h2>
        <ActivityList items={activity} />
      </section>
    </main>
  );
}

function ProfilePage({ member }: { member: AppSnapshot["member"] }) {
  return (
    <main id="main-content" className="page-stack">
      <header className="profile-header">
        <span className="profile-avatar profile-avatar--large" aria-hidden="true">{member.initials}</span>
        <div>
          <p className="eyebrow">Mi perfil</p>
          <h1>{member.fullName}</h1>
          <p>Miembro desde {member.memberSince}</p>
        </div>
      </header>

      <section className="membership-card" aria-labelledby="membership-title">
        <div>
          <span className="membership-card__label">Nivel actual</span>
          <h2 id="membership-title">{member.level}</h2>
        </div>
        <Icon name="sparkles" size={28} />
        <p><strong>{formatPoints(member.points)} puntos</strong> disponibles para tus próximas ventajas.</p>
      </section>

      <section aria-labelledby="account-title">
        <h2 className="section-title" id="account-title">Tu cuenta</h2>
        <div className="settings-list">
          <div><span><Icon name="user" size={20} /></span><div><strong>Datos personales</strong><small>Nombre, idioma y preferencias</small></div></div>
          <div><span><Icon name="bell" size={20} /></span><div><strong>Comunicaciones</strong><small>Noticias y notificaciones</small></div></div>
          <Link to="/showcase"><span><Icon name="phone" size={20} /></span><div><strong>Vista iPhone</strong><small>Modo de presentación comercial</small></div><Icon name="chevron" size={18} /></Link>
          <Link to="/system"><span><Icon name="settings" size={20} /></span><div><strong>Estado de la demo</strong><small>Información técnica y capacidades</small></div><Icon name="chevron" size={18} /></Link>
        </div>
      </section>
    </main>
  );
}

function IPhoneShowcase({ runtime }: { runtime: ResolvedDemoRuntime }) {
  return (
    <main className="showcase-page">
      <header className="showcase-toolbar">
        <div>
          <p className="eyebrow">Modo de presentación</p>
          <h1>{runtime.brand.name} en iPhone</h1>
        </div>
        <Link className="showcase-close" to="/">
          <Icon name="close" size={19} />
          <span>Salir</span>
        </Link>
      </header>

      <section
        className="iphone-stage"
        aria-label={`Simulación visual de ${runtime.brand.name} en un iPhone`}
      >
        <div className="iphone-device">
          <span className="iphone-device__speaker" aria-hidden="true" />
          <span className="iphone-device__button iphone-device__button--action" aria-hidden="true" />
          <span className="iphone-device__button iphone-device__button--volume-up" aria-hidden="true" />
          <span className="iphone-device__button iphone-device__button--volume-down" aria-hidden="true" />
          <span className="iphone-device__button iphone-device__button--power" aria-hidden="true" />
          <iframe
            className="iphone-device__screen"
            src={`/?demo=${encodeURIComponent(runtime.manifest.demoId)}`}
            title={`${runtime.brand.name} — vista iPhone`}
          />
          <span className="iphone-device__home-indicator" aria-hidden="true" />
        </div>
      </section>

      <p className="showcase-note">
        Simulación visual a 393 × 852 px. La validación en un iPhone real se realizará en A5.
      </p>
    </main>
  );
}

function SystemPage({
  runtime,
  snapshot,
  actionError,
  onPresenterAction,
}: {
  runtime: ResolvedDemoRuntime;
  snapshot: AppSnapshot;
  actionError?: string;
  onPresenterAction: () => void;
}) {
  if (snapshot.supervisionPerspective) {
    const supervision = snapshot.supervisionPerspective;
    return (
      <main id="main-content" className="adventure-page">
        <header className="adventure-heading">
          <p className="eyebrow">Supervisión</p>
          <h1 id="supervision-title">Estado de la aventura</h1>
          <p>Observa lo que cambia al actuar en «Mi aventura». Cambiar de vista conserva la sesión.</p>
        </header>
        <section className="adventure-guests" aria-label="Sujetos existentes">
          {supervision.subjects.map((subject) => (
            <article className="adventure-guest" key={subject.id}>
              <h2>{subject.id === "subject-p1" ? "P1 · Lucía" : "P2 · Huésped 2"}</h2>
              <p>{subject.id} · exists: {String(subject.exists)} · {subject.operationalState} · Evidence: {subject.evidenceCount}</p>
            </article>
          ))}
        </section>
        <section className="system-panel" aria-label="Evaluación compartida">
          <dl className="system-list">
            <div><dt>Cuenta/sesión operativa</dt><dd>{supervision.sessionSubjectRef}</dd></div>
            <div><dt>Criterio K</dt><dd>A AND (B OR C)</dd></div>
            <div><dt>Evidence recibida</dt><dd>{supervision.evidence.length}</dd></div>
            <div><dt>Admisibilidad conjunta</dt><dd>{supervision.jointAdmissibility}</dd></div>
            <div><dt>Suficiencia K</dt><dd>{supervision.sufficiency}</dd></div>
            <div><dt>Afirmación derivada</dt><dd>{supervision.derivedClaim}</dd></div>
          </dl>
        </section>
        <section aria-labelledby="evidence-title">
          <h2 id="evidence-title">Evidence y atribución</h2>
          {supervision.evidence.length === 0 ? <p>Todavía no hay Evidence. Alistarse o activar a un huésped no aporta pistas.</p> : (
            <ul className="adventure-evidence">{supervision.evidence.map((item) => <li key={item.id}>{item.id} · {item.subjectRefs.join(", ")} · {item.provenance}</li>)}</ul>
          )}
        </section>
      </main>
    );
  }
  const isOnline = navigator.onLine;
  const capabilityStatuses = [...new Set(runtime.capabilities.map(({ status }) => status))];
  const scriptStep = runtime.script?.steps.find(
    ({ action }) => action.actionId === snapshot.scenario?.availableActionId,
  ) ?? runtime.script?.steps[0];
  const actionAvailable =
    scriptStep?.action.actionId === snapshot.scenario?.availableActionId;

  return (
    <main id="main-content" className="page-stack">
      <header className="page-header page-header--internal">
        <p className="eyebrow">Panel interno</p>
        <h1>Estado de la demo</h1>
        <p>Información para preparar y verificar la demostración.</p>
      </header>
      <section className="system-panel" aria-label="Estado del sistema">
        <dl className="system-list">
          <div><dt>Demo</dt><dd>{runtime.manifest.demoId}</dd></div>
          <div><dt>Marca</dt><dd>{runtime.brand.name}</dd></div>
          <div><dt>Datos</dt><dd><span className="technical-badge">{capabilityStatuses.join(" + ")}</span></dd></div>
          <div><dt>Red</dt><dd>{isOnline ? "disponible" : "sin conexión"}</dd></div>
          <div><dt>Baseline</dt><dd>{runtime.experience?.tesBaseline ?? "No aplica a esta demo"}</dd></div>
          <div><dt>Futura</dt><dd>bloqueada hasta verificar licencia</dd></div>
        </dl>
      </section>
      {scriptStep && snapshot.scenario && (
        <section className="system-panel" aria-labelledby="presenter-action-title">
          <p className="eyebrow">Control de presentación</p>
          <h2 id="presenter-action-title">Escenario actual</h2>
          <dl className="system-list">
            <div><dt>Checkpoint</dt><dd>{snapshot.scenario.checkpoint}</dd></div>
            <div><dt>Resultado esperado</dt><dd>{scriptStep.expectedCheckpoint}</dd></div>
          </dl>
          <button
            className="secondary-action"
            type="button"
            disabled={!actionAvailable}
            onClick={onPresenterAction}
          >
            {scriptStep.presenterLabel}
          </button>
          {actionError && <p role="alert">{actionError}</p>}
        </section>
      )}
      <Link className="back-link" to="/profile"><Icon name="arrowBack" size={18} /> Volver al perfil</Link>
    </main>
  );
}

const navigation: { to: string; label: string; icon: IconName }[] = [
  { to: "/", label: "Inicio", icon: "home" },
  { to: "/benefits", label: "Beneficios", icon: "ticket" },
  { to: "/activity", label: "Actividad", icon: "activity" },
  { to: "/profile", label: "Perfil", icon: "user" },
];

function AppShell({
  snapshot,
  runtime,
  actionError,
  onPresenterAction,
  onReset,
}: {
  snapshot: AppSnapshot;
  runtime: ResolvedDemoRuntime;
  actionError?: string;
  onPresenterAction: () => void;
  onReset: () => void;
}) {
  const guestActionLabel = runtime.script?.steps.find(({ action }) => action.actionId === snapshot.scenario?.availableActionId)?.presenterLabel;
  const isAdventure = Boolean(snapshot.guestPerspective);
  const demoSearch = `?demo=${runtime.manifest.demoId}`;
  return (
    <div className={`app-shell${isAdventure ? " app-shell--adventure" : ""}`}>
      <a className="skip-link" href="#main-content">Saltar al contenido</a>
      <header className="topbar">
        <Link to={`/${demoSearch}`} aria-label="Ir al inicio">
          <img
            className="brand-logo"
            src={runtime.brand.logoUrl}
            alt={runtime.brand.name}
          />
        </Link>
        {isAdventure ? <span className="adventure-account">Cuenta de {snapshot.member.name}</span> : (
          <Link className="profile-avatar" to="/profile" aria-label="Abrir perfil">{snapshot.member.initials}</Link>
        )}
      </header>

      {isAdventure && (
        <>
          <nav className="adventure-nav" aria-label="Navegación de la aventura">
            <NavLink to={`/${demoSearch}`} end>Mi aventura</NavLink>
            <NavLink to={`/activity${demoSearch}`}>Actividad</NavLink>
            <NavLink to={`/system${demoSearch}`}>Supervisión</NavLink>
          </nav>
          {actionError && <p className="adventure-error" role="alert">{actionError}</p>}
        </>
      )}
      <Routes>
        <Route path="/" element={<HomePage snapshot={snapshot} guestAction={onPresenterAction} guestActionLabel={guestActionLabel} brandName={runtime.brand.name} introductoryFraming={runtime.script?.experimentalIntroductoryFraming} />} />
        <Route path="/benefits" element={<BenefitsPage coupons={snapshot.coupons} />} />
        <Route path="/activity" element={<ActivityPage activity={snapshot.activity} />} />
        <Route path="/profile" element={<ProfilePage member={snapshot.member} />} />
        <Route
          path="/system"
          element={
            <SystemPage
              runtime={runtime}
              snapshot={snapshot}
              actionError={actionError}
              onPresenterAction={onPresenterAction}
            />
          }
        />
        <Route path="*" element={<FeedbackState icon="compass" title="Esta página no existe" description="Vuelve al inicio para seguir explorando." action={{ label: "Ir al inicio", to: "/" }} />} />
      </Routes>

      {isAdventure ? (
        <footer className="adventure-tools">
          <p>Demo · hallazgos simulados</p>
          <button className="text-link" type="button" onClick={onReset}>Reiniciar aventura</button>
        </footer>
      ) : <nav className="bottom-nav" aria-label="Navegación principal">
        {navigation.map(({ to, label, icon }) => (
          <NavLink to={to} end={to === "/"} key={to}>
            <Icon name={icon} size={22} />
            <span>{label}</span>
          </NavLink>
        ))}
      </nav>}
    </div>
  );
}

export function App({ runtime }: { runtime: ResolvedDemoRuntime }) {
  const location = useLocation();
  const [snapshot, setSnapshot] = useState<AppSnapshot>();
  const [error, setError] = useState(false);
  const [actionError, setActionError] = useState<string>();

  useEffect(() => {
    runtime.provider.getSnapshot().then(setSnapshot).catch(() => setError(true));
  }, [runtime.provider]);

  if (location.pathname === "/showcase") {
    return <IPhoneShowcase runtime={runtime} />;
  }

  if (error) {
    return <FeedbackState icon="warning" title="No hemos podido cargar la App" description="Comprueba la conexión e inténtalo de nuevo." action={{ label: "Reintentar", onClick: () => window.location.reload() }} />;
  }

  if (!snapshot) {
    return <FeedbackState loading title="Preparando tu espacio" description="Estamos cargando tus beneficios." />;
  }

  const runPresenterAction = async () => {
    const step = runtime.script?.steps.find(
      ({ action }) => action.actionId === snapshot.scenario?.availableActionId,
    );
    if (!step) return;

    setActionError(undefined);
    try {
      setSnapshot(await runtime.provider.executeAction(step.action));
    } catch (actionFailure) {
      setActionError(
        actionFailure instanceof Error
          ? actionFailure.message
          : "No se pudo ejecutar la acción de presentación.",
      );
    }
  };

  return (
    <AppShell
      snapshot={snapshot}
      runtime={runtime}
      actionError={actionError}
      onPresenterAction={runPresenterAction}
      onReset={async () => {
        setActionError(undefined);
        try {
          setSnapshot(await runtime.provider.reset());
          document.getElementById("main-content")?.scrollIntoView?.({ block: "start" });
        }
        catch { setActionError("No se pudo reiniciar la aventura."); }
      }}
    />
  );
}
