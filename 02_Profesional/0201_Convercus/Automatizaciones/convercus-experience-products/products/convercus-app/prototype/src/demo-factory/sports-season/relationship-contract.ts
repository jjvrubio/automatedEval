// Situated product read contract. Independent of CSV, JSON and any future REST schema.
// CommerceTransaction is observed commerce, never a LoyaltyMovement.
export interface Person {
  id: string;
  name: string;
  customerRelationship: "established" | "not-established";
  knownData?: { city: string; usualSport: string };
}
export interface CommerceTransaction {
  id: string;
  personRef: string;
  occurredAt: string;
  channel: string;
  storeRef: string;
  currency: string;
  grossCents: number;
  category: string;
  product: string;
  quantity: number;
  unitCents: number;
  observedAt: string;
}
export interface LoyaltyLevel { id: string; name: string }
export interface LoyaltyState {
  personRef: string;
  membershipStatus: "non_member" | "active";
  membershipId: string | null;
  joinedAt: string | null;
  pointsBalance: number | null;
  actualLevel: LoyaltyLevel | null;
}
export interface LoyaltyCounterfactual {
  id: string;
  personRef: string;
  basisTransactionRefs: string[];
  basisCents: number;
  hypotheticalPoints: number;
  hypotheticalLevel: LoyaltyLevel;
  hypotheticalBenefits: string[];
  disclaimer: string;
  credited: false;
}
export interface RelationshipBadge {
  id: string;
  personRef: string;
  title: string;
  awardedAt: string;
  origin: "loyalty_program" | "sports_season";
  eventRef?: string;
  registrationRef?: string;
  supportingEvidenceRefs?: string[];
}
export interface Coupon {
  id: string;
  personRef: string;
  title: string;
  status: string;
  validFrom: string;
  validUntil: string;
}
export interface NewsItem { id: string; title: string; summary: string; publishedAt: string }
// Self Service projection only: does not redefine TES Experience.
export interface ExperienceSummary {
  id: string;
  personRef: string;
  name: string;
  state: "available" | "enrolled" | "active" | "completed";
  eligibility: string;
  eventRef?: string;
}
export interface NormalizedSportsData {
  people: Person[];
  transactions: CommerceTransaction[];
  loyaltyStates: LoyaltyState[];
  counterfactuals: LoyaltyCounterfactual[];
  badges: RelationshipBadge[];
  coupons: Coupon[];
  news: NewsItem[];
  experiences: ExperienceSummary[];
  program: {
    id: string;
    name: string;
    pointsPerFullEuro: number;
    levels: Array<LoyaltyLevel & { minPoints: number; maxPoints: number | null; benefits: string[] }>;
  };
}
export interface SportsDataAdapter {
  load(): NormalizedSportsData;
}
// Derived on read from shared person, commerce, loyalty and event records; never stored.
export interface PersonRelationship {
  program: NormalizedSportsData["program"];
  transactions: CommerceTransaction[];
  totalCents: number;
  loyalty: LoyaltyState;
  counterfactual?: LoyaltyCounterfactual;
  badges: RelationshipBadge[];
  coupons: Coupon[];
  news: NewsItem[];
  experiences: ExperienceSummary[];
}
