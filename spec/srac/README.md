# SRAC Vocabulary (Draft)

## Purpose

This vocabulary provides a minimal representation of product-specific safety relevance assertions for software components. 
The intent is to allow systems to exchange externally established safety relevance determinations without performing safety analysis or classification.

This vocabulary does not:

- determine safety relevance
- perform hazard analysis
- assign safety classifications
- replace domain-specific safety processes
Instead, it provides a mechanism to communicate existing decisions.
## Core Concepts
### ProductContext
A product configuration in which a safety relevance assertion applies.
### SoftwareComponent
A software element identified within a product.
### SafetyRelevanceAssertion
A product-specific assertion indicating whether a software component contributes to a safety-related function.
### SafetyClassification
An optional reference to a classification defined by an external safety framework.
Examples include:
- ISO 26262 ASIL levels
- IEC 62304 software safety classes
- DAL classifications
## Relationship
ProductContext
      │
      └── SafetyRelevanceAssertion ── SoftwareComponent
                      │
                      └── optional SafetyClassification

## Source and Licensing

This draft is an original, non-normative vocabulary contributed for evaluation by the COVESA community.

It does not reproduce normative text or controlled vocabularies from ISO, IEC, AUTOSAR, SPDX, CycloneDX, or other standards.

External safety frameworks are represented only through string-valued references. Any future vocabulary derived from another specification must identify the exact source, version, transformation, and applicable redistribution license.

