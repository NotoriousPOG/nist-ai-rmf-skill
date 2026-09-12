# Playbook pack — MANAGE

Use this file while scoring **MANAGE** subcategories. Prefer this over loading full `playbook.json`.

Count: **13**

## MANAGE 1.1

**Category:** `MANAGE-1`  
**Topics:** AI Deployment, Risk Assessment  
**AI Actors:** AI Deployment, Operation and Monitoring, AI Impact Assessment  

A determination is made as to whether the AI system achieves its intended purpose and stated objectives and whether its development or deployment should proceed.

### Suggested actions

- Consider trustworthiness characteristics when evaluating AI systems’ negative risks and benefits.
- Utilize TEVV outputs from map and measure functions when considering risk treatment.
- Regularly track and monitor negative risks and benefits throughout the AI system lifecycle including in post-deployment monitoring.
- Regularly assess and document system performance relative to trustworthiness characteristics and tradeoffs between negative risks and opportunities.
- Evaluate tradeoffs in connection with real-world use cases and impacts and as enumerated in Map function outcomes.

### Documentation / evidence prompts

### Organizations can document the following

- How do the technical specifications and requirements align with the AI system’s goals and objectives?
- To what extent are the metrics consistent with system goals, objectives, and constraints, including ethical and compliance considerations?
- What goals and objectives does the entity expect to achieve by designing, developing, and/or deploying the AI system?

### AI Transparency Resources

- GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities. [URL](https://www.gao.gov/products/gao-21-519sp)
- Artificial Intelligence Ethics Framework For The Intelligence Community. [URL](https://www.intelligence.gov/artificial-intelligence-ethics-framework-for-the-intelligence-community) 
- WEF Companion to the Model AI Governance Framework – Implementation and Self-Assessment Guide for Organizations [URL](https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/resource-for-organisation/ai/sgisago.ashx)

---

## MANAGE 1.2

**Category:** `MANAGE-1`  
**Topics:** Risk Tolerance  
**AI Actors:** AI Deployment, Operation and Monitoring, AI Impact Assessment  

Treatment of documented AI risks is prioritized based on impact, likelihood, or available resources or methods.

### Suggested actions

- Assign risk management resources relative to established risk tolerance. AI systems with lower risk tolerances receive greater oversight, mitigation and management resources. 
- Document AI risk tolerance determination practices and resource decisions.
- Regularly review risk tolerances and re-calibrate, as needed, in accordance with information from AI system monitoring and assessment .

### Documentation / evidence prompts

### Organizations can document the following

- Did your organization implement a risk management system to address risks involved in deploying the identified AI solution (e.g. personnel risk or changes to commercial objectives)?
- What assessments has the entity conducted on data security and privacy impacts associated with the AI system?
- Does your organization have an existing governance structure that can be leveraged to oversee the organization’s use of AI?

### AI Transparency Resources

- WEF Companion to the Model AI Governance Framework – Implementation and Self-Assessment Guide for Organizations [URL](https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/resource-for-organisation/ai/sgisago.ashx)
- GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities. [URL](https://www.gao.gov/products/gao-21-519sp)

---

## MANAGE 1.3

**Category:** `MANAGE-1`  
**Topics:** Legal and Regulatory, Risk Tolerance  
**AI Actors:** AI Deployment, Operation and Monitoring, AI Impact Assessment  

Responses to the AI risks deemed high priority as identified by the Map function, are developed, planned, and documented. Risk response options can include mitigating, transferring, avoiding, or accepting.

### Suggested actions

- Observe regulatory and established organizational, sector, discipline, or professional standards and requirements for applying risk tolerances within the organization.
- Document procedures for acting on AI system risks related to trustworthiness characteristics.
- Prioritize risks involving physical safety, legal liabilities, regulatory compliance, and negative impacts on individuals, groups, or society.
- Identify risk response plans and resources and organizational teams for carrying out response functions.
- Store risk management and system documentation in an organized, secure repository that is accessible by relevant AI Actors and appropriate personnel.

### Documentation / evidence prompts

### Organizations can document the following

- Has the system been reviewed to ensure the AI system complies with relevant laws, regulations, standards, and guidance?
- To what extent has the entity defined and documented the regulatory environment—including minimum requirements in laws and regulations?
- Did your organization implement a risk management system to address risks involved in deploying the identified AI solution (e.g. personnel risk or changes to commercial objectives)?

### AI Transparency Resources

- GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities. [URL](https://www.gao.gov/products/gao-21-519sp)
- Datasheets for Datasets. [URL](https://arxiv.org/abs/1803.09010)

---

## MANAGE 1.4

**Category:** `MANAGE-1`  
**Topics:** Risk Response  
**AI Actors:** AI Deployment, Operation and Monitoring, AI Impact Assessment  

Negative residual risks (defined as the sum of all unmitigated risks) to both downstream acquirers of AI systems and end users are documented.

### Suggested actions

- Document residual risks within risk response plans, denoting risks that have been accepted, transferred, or subject to minimal mitigation. 
- Establish procedures for disclosing residual risks to relevant downstream AI actors .
- Inform relevant downstream AI actors of requirements for safe operation, known limitations, and suggested warning labels as identified in MAP 3.4.

### Documentation / evidence prompts

### Organizations can document the following

- What are the roles, responsibilities, and delegation of authorities of personnel involved in the design, development, deployment, assessment and monitoring of the AI system?
- Who will be responsible for maintaining, re-verifying, monitoring, and updating this AI once deployed?
- How will updates/revisions be documented and communicated? How often and by whom?
- How easily accessible and current is the information available to external stakeholders?

### AI Transparency Resources

- GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities. [URL](https://www.gao.gov/products/gao-21-519sp)
- Artificial Intelligence Ethics Framework For The Intelligence Community. [URL](https://www.intelligence.gov/artificial-intelligence-ethics-framework-for-the-intelligence-community) 
- Datasheets for Datasets. [URL](https://arxiv.org/abs/1803.09010)

---

## MANAGE 2.1

**Category:** `MANAGE-2`  
**Topics:** Risk Tolerance, Trade-offs  
**AI Actors:** AI Deployment, Operation and Monitoring, AI Impact Assessment, Governance and Oversight  

Resources required to manage AI risks are taken into account, along with viable non-AI alternative systems, approaches, or methods – to reduce the magnitude or likelihood of potential impacts.

### Suggested actions

- Plan and implement risk management practices in accordance with established organizational risk tolerances.
- Verify risk management teams are resourced to carry out functions, including
	- Establishing processes for considering methods that are not automated; semi-automated; or other procedural alternatives for AI functions. 
	- Enhance AI system transparency mechanisms for AI teams.
	- Enable exploration of AI system limitations by AI teams.  
	- Identify, assess, and catalog past failed designs and negative impacts or outcomes to avoid known failure modes.
- Identify resource allocation approaches for managing risks in systems:
	- deemed high-risk,
	- that self-update (adaptive, online, reinforcement self-supervised learning or similar),
	- trained without access to ground truth (unsupervised, semi-supervised, learning or similar), 
	- with high uncertainty or where risk management is insufficient.
- Regularly seek and integrate external expertise and perspectives to supplement organizational diversity (e.g. demographic, disciplinary), equity, inclusion, and accessibility where internal capacity is lacking.
- Enable and encourage regular, open communication and feedback among AI actors and internal or external stakeholders related to system design or deployment decisions.
- Prepare and document plans for continuous monitoring and feedback mechanisms.

### Documentation / evidence prompts

### Organizations can document the following

- Are mechanisms in place to evaluate whether internal teams are empowered and resourced to effectively carry out risk management functions?
- How will user and other forms of stakeholder engagement be integrated into risk management processes?

### AI Transparency Resources

- Artificial Intelligence Ethics Framework For The Intelligence Community. [URL](https://www.intelligence.gov/artificial-intelligence-ethics-framework-for-the-intelligence-community) 
- Datasheets for Datasets. [URL](https://arxiv.org/abs/1803.09010)
- GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities. [URL](https://www.gao.gov/products/gao-21-519sp)

---

## MANAGE 2.2

**Category:** `MANAGE-2`  
**Topics:** AI Deployment, Drift, Societal Values  
**AI Actors:** AI Deployment, Operation and Monitoring, AI Impact Assessment, Governance and Oversight  

Mechanisms are in place and applied to sustain the value of deployed AI systems.

### Suggested actions

- Establish risk controls considering trustworthiness characteristics, including:
        - Data management, quality, and privacy (e.g. minimization, rectification or deletion requests) controls as part of organizational data governance policies. 
        - Machine learning and end-point security countermeasures (e.g., robust models, differential privacy, authentication, throttling).
        - Business rules that augment, limit or restrict AI system outputs within certain contexts 
        - Utilizing domain expertise related to deployment context for continuous improvement and TEVV across the AI lifecycle.
        - Development and regular tracking of human-AI teaming configurations.
        - Model assessment and test, evaluation, validation and verification (TEVV) protocols.
        - Use of standardized documentation and transparency mechanisms.
        - Software quality assurance practices across AI lifecycle.
        - Mechanisms to explore system limitations and avoid past failed designs or deployments.
- Establish mechanisms to capture feedback from system end users and potentially impacted groups while system is in deployment.
-Establish mechanisms to capture feedback from system end users and potentially impacted groups about how changes in system deployment (e.g.,  introducing new technology, decommissioning algorithms and models, adapting system, model or algorithm) may create negative impacts that are not visible along the AI lifecycle.
- Review insurance policies, warranties, or contracts for legal or oversight requirements for risk transfer procedures.
- Document risk tolerance decisions and risk acceptance procedures.

### Documentation / evidence prompts

### Organizations can document the following

- To what extent can users or parties affected by the outputs of the AI system test the AI system and provide feedback?
- Could the AI system expose people to harm or negative impacts? What was done to mitigate or reduce the potential for harm?
- How will the accountable human(s) address changes in accuracy and precision due to either an adversary’s attempts to disrupt the AI or unrelated changes in the operational or business environment?

### AI Transparency Resources

- GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities. [URL](https://www.gao.gov/products/gao-21-519sp)
- Artificial Intelligence Ethics Framework For The Intelligence Community. [URL](https://www.intelligence.gov/artificial-intelligence-ethics-framework-for-the-intelligence-community)

---

## MANAGE 2.3

**Category:** `MANAGE-2`  
**Topics:** Risk Response  
**AI Actors:** AI Deployment, Operation and Monitoring  

Procedures are followed to respond to and recover from a previously unknown risk when it is identified.

### Suggested actions

- Protocols, resources, and metrics  are in place for continual monitoring of AI systems’ performance, trustworthiness, and alignment with contextual norms and values 
- Establish and regularly review treatment and response plans for incidents, negative impacts, or outcomes.
- Establish and maintain procedures to regularly monitor system components for drift, decontextualization, or other AI system behavior factors, 
- Establish and maintain procedures for capturing feedback about negative impacts.
- Verify contingency processes to handle any negative impacts associated with mission-critical AI systems, and to deactivate systems.
- Enable preventive and post-hoc exploration of AI system limitations by relevant AI actor groups.
- Decommission systems that exceed risk tolerances.

### Documentation / evidence prompts

### Organizations can document the following

- Who will be responsible for maintaining, re-verifying, monitoring, and updating this AI once deployed?
- Are the responsibilities of the personnel involved in the various AI governance processes clearly defined? (Including responsibilities to decommission the AI system.)
- What processes exist for data generation, acquisition/collection, ingestion, staging/storage, transformations, security, maintenance, and dissemination?
- How will the appropriate performance metrics, such as accuracy, of the AI be monitored after the AI is deployed? 

### AI Transparency Resources

- Artificial Intelligence Ethics Framework For The Intelligence Community. [URL](https://www.intelligence.gov/artificial-intelligence-ethics-framework-for-the-intelligence-community) 
- WEF - Companion to the Model AI Governance Framework – Implementation and Self-Assessment Guide for Organizations. [URL](https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/resource-for-organisation/ai/sgisago.ashx)
- GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities. [URL](https://www.gao.gov/products/gao-21-519sp)

---

## MANAGE 2.4

**Category:** `MANAGE-2`  
**Topics:** Risk Response, Decommission, Risky Emergent Behavior  
**AI Actors:** AI Deployment, Operation and Monitoring, Governance and Oversight  

Mechanisms are in place and applied, responsibilities are assigned and understood to supersede, disengage, or deactivate AI systems that demonstrate performance or outcomes inconsistent with intended use.

### Suggested actions

- Regularly review established procedures for AI system bypass actions, including plans for redundant or backup systems to ensure continuity of operational and/or business functionality.
- Regularly review Identify system incident thresholds for activating bypass or deactivation responses.
- Apply change management processes to understand the upstream and downstream consequences of bypassing or deactivating an AI system or AI system components.
- Apply protocols, resources and metrics for decisions to supersede, bypass or deactivate AI systems or AI system components.
- Preserve materials for forensic, regulatory, and legal review.
- Conduct internal root cause analysis and process reviews of bypass or deactivation events. 
- Decommission and preserve system components that cannot be updated to meet criteria for redeployment.
- Establish criteria for redeploying updated system components, in consideration of trustworthy characteristics

### Documentation / evidence prompts

### Organizations can document the following

- What are the roles, responsibilities, and delegation of authorities of personnel involved in the design, development, deployment, assessment and monitoring of the AI system?
- Did your organization implement a risk management system to address risks involved in deploying the identified AI solution (e.g. personnel risk or changes to commercial objectives)?
- What testing, if any, has the entity conducted on the AI system to identify errors and limitations (i.e. adversarial or stress testing)?
- To what extent does the entity have established procedures for retiring the AI system, if it is no longer needed?
- How did the entity use assessments and/or evaluations to determine if the system can be scaled up, continue, or be decommissioned?

### AI Transparency Resources

- GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities. [URL](https://www.gao.gov/products/gao-21-519sp)

---

## MANAGE 3.1

**Category:** `MANAGE-3`  
**Topics:** Third-party, Supply Chain  
**AI Actors:** Third-party entities, Operation and Monitoring, AI Deployment  

AI risks and benefits from third-party resources are regularly monitored, and risk controls are applied and documented.

### Suggested actions

- Have legal requirements been addressed?
- Apply organizational risk tolerance to third-party AI systems.
- Apply and document organizational risk management plans and practices to third-party AI technology, personnel, or other resources.
- Identify and maintain documentation for third-party AI systems and components.
- Establish testing, evaluation, validation and verification processes for third-party AI systems which address the needs for transparency without exposing proprietary algorithms .
- Establish processes to identify beneficial use and risk indicators in third-party systems or components, such as inconsistent software release schedule, sparse documentation, and incomplete software change management (e.g., lack of forward or backward compatibility).
- Organizations can establish processes for third parties to report known and potential vulnerabilities, risks or biases in supplied resources.
- Verify contingency processes for handling negative impacts associated with mission-critical third-party AI systems.
- Monitor third-party AI systems for potential negative impacts and risks associated with trustworthiness characteristics.
- Decommission third-party systems that exceed risk tolerances.

### Documentation / evidence prompts

### Organizations can document the following

- If a third party created the AI system or some of its components, how will you ensure a level of explainability or interpretability? Is there documentation?
- If your organization obtained datasets from a third party, did your organization assess and manage the risks of using such datasets?
- Did you establish a process for third parties (e.g. suppliers, end users, subjects, distributors/vendors or workers) to report potential vulnerabilities, risks or biases in the AI system?
- Have legal requirements been addressed?

### AI Transparency Resources

- Artificial Intelligence Ethics Framework For The Intelligence Community. [URL](https://www.intelligence.gov/artificial-intelligence-ethics-framework-for-the-intelligence-community)
- WEF - Companion to the Model AI Governance Framework – Implementation and Self-Assessment Guide for Organizations. [URL](https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/resource-for-organisation/ai/sgisago.ashx)
- Datasheets for Datasets. [URL](https://arxiv.org/abs/1803.09010)

---

## MANAGE 3.2

**Category:** `MANAGE-3`  
**Topics:** Pre-trained models, Monitoring  
**AI Actors:** Third-party entities, Operation and Monitoring, AI Deployment  

Pre-trained models which are used for development are monitored as part of AI system regular  monitoring and maintenance.

### Suggested actions

- Identify pre-trained models within AI system inventory for risk tracking.
- Establish processes to independently and continually monitor performance and trustworthiness  of pre-trained models, and as part of third-party risk tracking. 
- Monitor performance and trustworthiness of AI system components connected to pre-trained models, and as part of third-party risk tracking.
- Identify, document and remediate risks arising from AI system components and pre-trained models per organizational risk management procedures, and as part of third-party risk tracking.
- Decommission AI system components and pre-trained models which exceed risk tolerances, and as part of third-party risk tracking.

### Documentation / evidence prompts

### Organizations can document the following

- How has the entity documented the AI system’s data provenance, including sources, origins, transformations, augmentations, labels, dependencies, constraints, and metadata?
- Does this dataset collection/processing procedure achieve the motivation for creating the dataset stated in the first section of this datasheet?
- How does the entity ensure that the data collected are adequate, relevant, and not excessive in relation to the intended purpose?
- If the dataset becomes obsolete how will this be communicated?

### AI Transparency Resources

- Artificial Intelligence Ethics Framework For The Intelligence Community. [URL](https://www.intelligence.gov/artificial-intelligence-ethics-framework-for-the-intelligence-community)
- WEF - Companion to the Model AI Governance Framework – Implementation and Self-Assessment Guide for Organizations. [URL](https://www.pdpc.gov.sg/-/media/files/pdpc/pdf-files/resource-for-organisation/ai/sgisago.ashx)
- Datasheets for Datasets. [URL](https://arxiv.org/abs/1803.09010)

---

## MANAGE 4.1

**Category:** `MANAGE-4`  
**Topics:** Monitoring, Participation, AI Deployment, AI Incidents, Risk Response, Adversarial, Risky Emergent Behavior  
**AI Actors:** AI Deployment, Operation and Monitoring, End-Users, Human Factors, Domain Experts, Affected Individuals and Communities  

Post-deployment AI system monitoring plans are implemented, including mechanisms for capturing and evaluating input from users and other relevant AI actors, appeal and override, decommissioning, incident response, recovery, and change management.

### Suggested actions

- Establish and maintain procedures to monitor AI system performance for risks and negative and positive impacts associated with trustworthiness characteristics. 
- Perform post-deployment TEVV tasks to evaluate AI system validity and reliability, bias and fairness, privacy, and security and resilience.
- Evaluate AI system trustworthiness in conditions similar to deployment context of use, and prior to deployment.
- Establish and implement red-teaming exercises at a prescribed cadence, and evaluate their efficacy. 
- Establish procedures for tracking dataset modifications such as data deletion or rectification requests.
- Establish mechanisms for regular communication and feedback between relevant AI actors and internal or external stakeholders to capture information about system performance, trustworthiness and impact.
- Share information about errors, near-misses, and attack patterns with incident databases, other organizations with similar systems, and system users and stakeholders.
- Respond to and document detected or reported negative impacts or issues in AI system performance and trustworthiness.
- Decommission systems that exceed establish risk tolerances.

### Documentation / evidence prompts

### Organizations can document the following

- To what extent has the entity documented the post-deployment AI system’s testing methodology, metrics, and performance outcomes?
- How easily accessible and current is the information available to external stakeholders?

### AI Transparency Resources

- GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities, [URL](https://www.gao.gov/products/gao-21-519sp)
- Datasheets for Datasets. [URL](https://arxiv.org/abs/1803.09010)

---

## MANAGE 4.2

**Category:** `MANAGE-4`  
**Topics:** Monitoring, Impact Assessment, Risk Assessment, Continual Improvement  
**AI Actors:** TEVV, AI Design, AI Development, AI Deployment, Operation and Monitoring, End-Users, Affected Individuals and Communities  

Measurable activities for continual improvements are integrated into AI system updates and include regular engagement with interested parties, including relevant AI actors.

### Suggested actions

- Integrate trustworthiness characteristics into protocols and metrics used for continual improvement.
- Establish processes for evaluating and integrating feedback into AI system improvements.
- Assess and evaluate alignment of proposed improvements with relevant regulatory and legal frameworks
- Assess and evaluate alignment of proposed improvements connected to the values and norms within the context of use.
- Document the basis for decisions made relative to tradeoffs between trustworthy characteristics, system risks, and system opportunities

### Documentation / evidence prompts

### Organizations can document the following

- How will user and other forms of stakeholder engagement be integrated into the model development process and regular performance review once deployed?
- To what extent can users or parties affected by the outputs of the AI system test the AI system and provide feedback?
- To what extent has the entity defined and documented the regulatory environment—including minimum requirements in laws and regulations?

### AI Transparency Resources

- GAO-21-519SP - Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities, [URL](https://www.gao.gov/products/gao-21-519sp)
- Artificial Intelligence Ethics Framework For The Intelligence Community. [URL](https://www.intelligence.gov/artificial-intelligence-ethics-framework-for-the-intelligence-community)

---

## MANAGE 4.3

**Category:** `MANAGE-4`  
**Topics:** AI Incidents, Monitoring  
**AI Actors:** AI Deployment, Operation and Monitoring, End-Users, Human Factors, Domain Experts, Affected Individuals and Communities  

Incidents and errors are communicated to relevant AI actors including affected communities. Processes for tracking, responding to, and recovering from incidents and errors are followed and documented.

### Suggested actions

- Establish procedures to regularly share information about errors, incidents and negative impacts with relevant stakeholders, operators, practitioners and users, and impacted parties.
- Maintain a database of reported errors, near-misses, incidents and negative impacts including date reported, number of reports, assessment of impact and severity, and responses.
- Maintain a database of system changes, reason for change, and details of how the change was made, tested and deployed. 
- Maintain version history information and metadata to enable continuous improvement processes.
- Verify that relevant AI actors responsible for identifying complex or emergent risks are properly resourced and empowered.

### Documentation / evidence prompts

### Organizations can document the following

- What corrective actions has the entity taken to enhance the quality, accuracy, reliability, and representativeness of the data?
- To what extent does the entity communicate its AI strategic goals and objectives to the community of stakeholders? How easily accessible and current is the information available to external stakeholders?
- What type of information is accessible on the design, operations, and limitations of the AI system to external stakeholders, including end users, consumers, regulators, and individuals impacted by use of the AI system?

### AI Transparency Resources

- GAO-21-519SP: Artificial Intelligence: An Accountability Framework for Federal Agencies & Other Entities, [URL](https://www.gao.gov/products/gao-21-519sp)

---
