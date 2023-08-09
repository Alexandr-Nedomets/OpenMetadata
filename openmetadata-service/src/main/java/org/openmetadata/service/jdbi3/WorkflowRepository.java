package org.openmetadata.service.jdbi3;

import static org.openmetadata.service.Entity.WORKFLOW;

import org.openmetadata.schema.entity.automations.Workflow;
import org.openmetadata.schema.services.connections.metadata.OpenMetadataConnection;
import org.openmetadata.service.resources.automations.WorkflowResource;
import org.openmetadata.service.secrets.SecretsManager;
import org.openmetadata.service.secrets.SecretsManagerFactory;
import org.openmetadata.service.util.EntityUtil;

public class WorkflowRepository extends EntityRepository<Workflow> {
  private static final String PATCH_FIELDS = "status,response";

  public WorkflowRepository(CollectionDAO dao) {
    super(WorkflowResource.COLLECTION_PATH, WORKFLOW, Workflow.class, dao.workflowDAO(), dao, PATCH_FIELDS, "");
    quoteFqn = true;
  }

  @Override
  public Workflow setFields(Workflow entity, EntityUtil.Fields fields) {
    return entity;
  }

  @Override
  public Workflow clearFields(Workflow entity, EntityUtil.Fields fields) {
    return entity;
  }

  @Override
  public void prepare(Workflow entity) {
    // validate request and status
    if (entity.getRequest() == null) {
      throw new IllegalArgumentException("Request must not be empty");
    }
  }

  @Override
  public void storeEntity(Workflow entity, boolean update) {
    OpenMetadataConnection openmetadataConnection = entity.getOpenMetadataServerConnection();
    SecretsManager secretsManager = SecretsManagerFactory.getSecretsManager();

    if (secretsManager != null) {
      entity = secretsManager.encryptWorkflow(entity);
    }

    // Don't store owner, database, href and tags as JSON. Build it on the fly based on relationships
    entity.withOpenMetadataServerConnection(null);
    store(entity, update);

    // Restore the relationships
    entity.withOpenMetadataServerConnection(openmetadataConnection);
  }

  /** Remove the secrets from the secret manager */
  @Override
  protected void postDelete(Workflow workflow) {
    SecretsManagerFactory.getSecretsManager().deleteSecretsFromWorkflow(workflow);
  }

  @Override
  public void storeRelationships(Workflow entity) {
    // No relationships to store beyond what is stored in the super class
  }

  @Override
  public EntityUpdater getUpdater(Workflow original, Workflow updated, Operation operation) {
    return new WorkflowUpdater(original, updated, operation);
  }

  public class WorkflowUpdater extends EntityUpdater {
    public WorkflowUpdater(Workflow original, Workflow updated, Operation operation) {
      super(original, updated, operation);
    }

    @Override
    public void entitySpecificUpdate() {
      recordChange("status", original.getStatus(), updated.getStatus());
      recordChange("response", original.getResponse(), updated.getResponse(), true);
    }
  }
}
