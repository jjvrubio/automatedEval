import type { DataAdapter, SignificantEvent } from "@/domain/contracts";
import type { IconName } from "@/ui/Icon";

export interface Coupon {
  id: string;
  title: string;
  description: string;
  validUntil: string;
  tag: string;
  tone: "cyan" | "pink" | "blue";
  icon: IconName;
}

export interface ActivityItem {
  id: string;
  title: string;
  description: string;
  occurredAt: string;
  displayDate: string;
  points?: number;
  tone: "cyan" | "pink" | "blue";
  icon: IconName;
}

export interface AppSnapshot {
  member: {
    id: string;
    name: string;
    fullName: string;
    initials: string;
    level: string;
    nextLevel: string;
    points: number;
    progress: number;
    pointsToNextLevel: number;
    memberSince: string;
  };
  coupons: Coupon[];
  news: {
    id: string;
    category: string;
    title: string;
    summary: string;
  }[];
  activity: ActivityItem[];
}

const initialSnapshot: AppSnapshot = {
  member: {
    id: "member-demo-001",
    name: "Alex",
    fullName: "Alex Martín",
    initials: "AM",
    level: "Essential",
    nextLevel: "Plus",
    points: 1_240,
    progress: 62,
    pointsToNextLevel: 760,
    memberSince: "marzo de 2024",
  },
  coupons: [
    {
      id: "coupon-welcome",
      title: "20% de bienvenida",
      description: "Disfruta tu ventaja en la próxima compra.",
      validUntil: "Hasta el 30 ago",
      tag: "Para ti",
      tone: "cyan",
      icon: "gift",
    },
    {
      id: "coupon-double-points",
      title: "Puntos x2",
      description: "Duplica tus puntos durante todo el fin de semana.",
      validUntil: "Este fin de semana",
      tag: "Especial",
      tone: "pink",
      icon: "sparkles",
    },
    {
      id: "coupon-member",
      title: "Envío sin coste",
      description: "Una ventaja exclusiva por ser miembro Essential.",
      validUntil: "Hasta el 15 sep",
      tag: "Essential",
      tone: "blue",
      icon: "ticket",
    },
  ],
  news: [
    {
      id: "news-new-season",
      category: "Novedades",
      title: "Una nueva temporada para descubrir",
      summary: "Ideas, ventajas y experiencias elegidas para acompañarte.",
    },
  ],
  activity: [
    {
      id: "activity-purchase",
      title: "Compra registrada",
      description: "Tus puntos ya están disponibles.",
      occurredAt: "2026-08-02T17:30:00Z",
      displayDate: "Ayer, 17:30",
      points: 120,
      tone: "cyan",
      icon: "star",
    },
    {
      id: "activity-coupon",
      title: "Nuevo beneficio",
      description: "Has recibido tu cupón de bienvenida.",
      occurredAt: "2026-08-01T09:15:00Z",
      displayDate: "1 ago, 09:15",
      tone: "pink",
      icon: "gift",
    },
    {
      id: "activity-profile",
      title: "Perfil actualizado",
      description: "Tus preferencias se han guardado correctamente.",
      occurredAt: "2026-07-28T11:00:00Z",
      displayDate: "28 jul, 11:00",
      tone: "blue",
      icon: "user",
    },
  ],
};

export class MockDataAdapter implements DataAdapter<AppSnapshot, SignificantEvent> {
  readonly mode = "mock" as const;
  private snapshot = structuredClone(initialSnapshot);

  async getSnapshot(): Promise<AppSnapshot> {
    return structuredClone(this.snapshot);
  }

  async dispatch(event: SignificantEvent): Promise<AppSnapshot> {
    this.snapshot.activity.unshift({
      id: event.id,
      title: event.type,
      description: `Evento recibido desde ${event.source}.`,
      occurredAt: event.occurredAt,
      displayDate: event.occurredAt,
      tone: "blue",
      icon: "activity",
    });
    return this.getSnapshot();
  }

  async reset(): Promise<AppSnapshot> {
    this.snapshot = structuredClone(initialSnapshot);
    return this.getSnapshot();
  }
}
